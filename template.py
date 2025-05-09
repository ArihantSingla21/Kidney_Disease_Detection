import sys 
import os 
import logging 
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

Project_name = "cnnClassifier"

list_of_files = [
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/config/configuration.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/constants/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/exception/__init__.py",
    f"src/{Project_name}/logger/__init__.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/utils/__init__.py",
    "configuration.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "README.md",
    "setup.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "templates/index.html",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")


logging.info(f"Project Name: {Project_name} structure is created successfully")