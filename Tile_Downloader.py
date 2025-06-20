# Tile downloader for Google Street View panoramas
# Usage:
#   from tile_downloader import download_panorama
#   download_panorama('PANO_ID_HERE', 'output.jpg', zoom=5)

import os
import math
import requests
import numpy as np
from io import BytesIO
from PIL import Image
from utils import resolve_path

from dotenv import load_dotenv
load_dotenv(resolve_path("secrets.env"))

from AppLogger import Logger
logger = Logger(__name__)

from config_ import Config
config = Config(logger)

region = config.get_general_data()['region']


def fetch_cube_faces(pano_id: str):
    """
    Fetch the six cube faces from the Static API:
      headings 0,90,180,270 at pitch=0 → front, right, back, left
      plus pitch=+90 (up) and pitch=-90 (down)
    Returns dict of PIL Images.
    """
    BASE_URL = "https://maps.googleapis.com/maps/api/streetview"
    FACE_SIZE = int(config.get_download_data()['face_size'])
    params = {
        "size": f"{FACE_SIZE}x{FACE_SIZE}",
        "pano": pano_id,
        "fov": 90,
        "key": os.getenv("API_KEY")
    }
    faces = {}
    # equator faces
    for heading, name in [(0, "front"), (90, "right"), (180, "back"), (270, "left")]:
        params.update({"heading": heading, "pitch": 0})
        resp = requests.get(BASE_URL, params=params)
        resp.raise_for_status()
        faces[name] = Image.open(BytesIO(resp.content))
    # up/down
    for pitch, name in [(90, "up"), (-90, "down")]:
        params.update({"heading": 0, "pitch": pitch})
        resp = requests.get(BASE_URL, params=params)
        resp.raise_for_status()
        faces[name] = Image.open(BytesIO(resp.content))
    return faces

def orient_faces(faces: dict[str,Image.Image]) -> dict[str,Image.Image]:
    """
    Rotate/flip the raw cube faces so that sampling them with your existing
    uc/vc math produces correctly oriented output.
    """
    faces["front"] = faces["front"].rotate(180, expand=False)
    faces["back"]  = faces["back"].rotate(180,  expand=False)
    faces["left"]  = faces["left"].rotate(180, expand=False)
    faces["right"] = faces["right"].rotate(180, expand=False)
    return faces

def cube_to_equirectangular(faces: dict, FACE_SIZE = int(config.get_download_data()['face_size'])):
    """
    Reproject 6 cube faces (dict with keys front, right, back, left, up, down)
    into one equirectangular image of size (4*FACE_SIZE, 2*FACE_SIZE).
    """
    W = 4 * FACE_SIZE
    H = 2 * FACE_SIZE
    # Prepare output pixel grid
    ys, xs = np.indices((H, W), dtype=np.float32)
    lon = (xs / W) * 2 * math.pi - math.pi
    lat = math.pi/2 - (ys / H) * math.pi

    # Convert spherical to Cartesian
    x = np.cos(lat) * np.cos(lon)
    y = np.cos(lat) * np.sin(lon)
    z = np.sin(lat)

    # Which face?
    abs_x, abs_y, abs_z = np.abs(x), np.abs(y), np.abs(z)
    # Initialize empty arrays
    out = np.zeros((H, W, 3), dtype=np.uint8)

    def sample(face_img, uc, vc):
        # uc, vc are floats in [-1,1] for face coords → map to [0, FACE_SIZE)
        u = ((uc + 1) / 2) * (FACE_SIZE - 1)
        v = ((vc + 1) / 2) * (FACE_SIZE - 1)
        u = np.clip(np.round(u).astype(int), 0, FACE_SIZE-1)
        v = np.clip(np.round(v).astype(int), 0, FACE_SIZE-1)
        arr = np.array(face_img)
        return arr[v, u]

    faces = orient_faces(faces=faces)

    # Front face: +X major
    mask = (abs_x >= abs_y) & (abs_x >= abs_z) & (x > 0)
    uc = -y[mask] / abs_x[mask]
    vc =  z[mask] / abs_x[mask]
    out[mask] = sample(faces["front"], uc, vc)

    # Back face: -X major
    mask = (abs_x >= abs_y) & (abs_x >= abs_z) & (x < 0)
    uc =  y[mask] / abs_x[mask]
    vc =  z[mask] / abs_x[mask]
    out[mask] = sample(faces["back"], uc, vc)

    # Right face: +Y major
    mask = (abs_y > abs_x) & (abs_y >= abs_z) & (y > 0)
    uc =  x[mask] / abs_y[mask]
    vc =  z[mask] / abs_y[mask]
    out[mask] = sample(faces["right"], uc, vc)

    # Left face: -Y major
    mask = (abs_y > abs_x) & (abs_y >= abs_z) & (y < 0)
    uc = -x[mask] / abs_y[mask]
    vc =  z[mask] / abs_y[mask]
    out[mask] = sample(faces["left"], uc, vc)

    # Up face: +Z major
    mask = (abs_z > abs_x) & (abs_z > abs_y) & (z > 0)
    uc =  y[mask] / abs_z[mask]
    vc =  x[mask] / abs_z[mask]
    out[mask] = sample(faces["up"], uc, vc)

    # Down face: -Z major
    mask = (abs_z > abs_x) & (abs_z > abs_y) & (z < 0)
    uc =  y[mask] / abs_z[mask]
    vc = -x[mask] / abs_z[mask]
    out[mask] = sample(faces["down"], uc, vc)

    return Image.fromarray(out)

def download_panorama(pano_id: str, save_dir: str, coords: tuple[float,float], face):
    region = config.get_general_data()['region']
    logger.log_status("Started Panaroma Download")
    try:
        faces = fetch_cube_faces(pano_id)
        eq = cube_to_equirectangular(faces, face)
        print(bool(eq))
        lat, lng = coords
        os.makedirs(save_dir, exist_ok=True)
        filename = f"{region}_{pano_id}_{lat}_{lng}_360.jpg"
        path = os.path.join(save_dir, filename)
        eq.save(path, "JPEG")
        logger.log_status(f"Panaromas Downloaded successfully to {path}")
        print(path)
    except Exception as e:
        logger.log_exception(f"Error while downloading Panaromas: {e}")
