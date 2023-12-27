#This script is to create the tempelate in one click rather than doing to tediously!


import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath) #handling path conversions from linux to windows
    filedir, filename = os.path.split(filepath)

    if filedir !="": #Checking if directory exists
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #checking if file exists
        with open(filepath, 'w') as f:
            pass
        logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f"{filename} already exists")