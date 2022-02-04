from typing import Optional

def openFile(location: str) -> str:
    with open(location) as f:
        filed = f.read()

    return filed