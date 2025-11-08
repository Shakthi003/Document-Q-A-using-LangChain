import os
from pathlib import Path

DATA_DIR = Path("data")
DB_DIR = Path("db")

def ensure_dirs():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DB_DIR.mkdir(parents=True, exist_ok=True)

def cleanup_uploaded_files():
    """Remove files inside data/ — call only when safe."""
    for f in DATA_DIR.glob("*"):
        try:
            f.unlink()
        except Exception:
            pass
