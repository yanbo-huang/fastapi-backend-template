import os
import shutil
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    shutil.copy(src=Path(ROOT_DIR) / "local.env", dst=Path(ROOT_DIR) / ".env")
