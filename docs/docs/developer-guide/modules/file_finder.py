from pathlib import Path

Foldr = r"C:\Users\lenovo\Desktop\pyQT\docs\docs\developer-guide\modules"
for file in Path(Foldr).glob("*.md"):
    print(f'/{file.stem}.py:    # ')
