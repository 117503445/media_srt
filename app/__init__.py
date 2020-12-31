import pathlib
from app import path
from htutil import file

for f in path.dirs:
    file.create_dir_if_not_exist(f)
