from pathlib import Path
import os
import logging

files = [
    "src/__init__.py",
    "src/helper.py",
    "setup.py",
    "research/snippets.ipynb",
    "requirements.txt",
    ".env"
    
]

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s]')

for filepath in files:
    filepath = Path(filepath)
    dir_, file = os.path.split(filepath)

    if dir_ != "":
        if not os.path.exists(dir_):
            os.makedirs(dir_)
            logging.info(f"Directory Created: {dir_}")
        
        else:
            logging.info(f"Directory Already Exists")
        
    if not filepath.exists():
        with open(filepath,"w") as f:
            pass
        logging.info(f"file created: {filepath}")

    elif os.path.getsize(str(filepath)) == 0:
        logging.info(f"File Already Exists But Empty {filepath}")
    
    else:
        logging.info(f"File already exists")


