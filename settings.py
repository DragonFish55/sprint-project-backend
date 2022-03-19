import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent

ROOT_LIST = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PATH = os.path.join(ROOT_DIR, "/app")