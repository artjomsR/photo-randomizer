import os, sys, glob, random, distutils, shutil
from pathlib import Path
# import numpy as np

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    print(f'copying {from_path} to {to_path}...')
    shutil.copytree(from_path, to_path)


maximum_no_of_files = 1735
original_dir = 'D:\JPG Export\Photo Frame\Sorted'
walk_dir = 'D:\PHOTOFRAME_PHOTOS_DELETE_ME'

if not (os.path.isdir(original_dir)):
	input(f'{original_dir} does not exist, aborting...')
	sys.exit()

copy_and_overwrite(original_dir, walk_dir)

total_files = len(list(Path(walk_dir).rglob("*.jpg")))
deletion_coefficient = maximum_no_of_files / total_files
print(f'Total files:{total_files}, deletion_coefficient = {deletion_coefficient}')

for root, subdirs, files in os.walk(walk_dir):
	for subdir in subdirs:
		print(os.path.join(root, subdir))
		os.chdir(os.path.join(root, subdir))
		folder_jpgs = glob.glob("*.jpg")
		if len(folder_jpgs) > 4:
			no_of_files_to_delete = len(folder_jpgs) - int(len(folder_jpgs) * deletion_coefficient)
			print(f'files:{len(folder_jpgs)}, files to delete:{no_of_files_to_delete}')
			for file in random.sample(folder_jpgs, no_of_files_to_delete):
				os.remove(file)

input("DONE")