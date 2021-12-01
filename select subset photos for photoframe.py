import os, sys, glob, random, distutils, shutil
from pathlib import Path
from typing import DefaultDict

maximum_no_of_files = 1735
minimum_number_of_files_to_be_trimmed = 4
original_dir = 'E:\JPG Export\Photo Frame\Sorted'
trim_dir = 'E:/PHOTOFRAME_PHOTOS_DELETE_ME'
folder_separator = '-- '

def copy_folder_with_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    print(f'copying {from_path} to {to_path}...')
    shutil.copytree(from_path, to_path)

def folder_structure_is_flat(path):
	return len(os.listdir(path)) > maximum_no_of_files

def put_files_in_subfolders(source_dir_path):
	for combined_filename in os.listdir(source_dir_path):
		basename, extension = os.path.splitext(combined_filename)
		parent_folder = basename.split(folder_separator)
		
		path_to_parent_folder = f'{source_dir_path}\{parent_folder[0]}';
		if not os.path.exists(path_to_parent_folder):
			os.makedirs(path_to_parent_folder)
		shutil.move(f'{source_dir_path}\{combined_filename}', f'{path_to_parent_folder}\{combined_filename}')


if not (os.path.isdir(original_dir)):
	input(f'{original_dir} does not exist, aborting...')
	sys.exit()

copy_folder_with_overwrite(original_dir, trim_dir)

if folder_structure_is_flat(trim_dir):
	put_files_in_subfolders(trim_dir)

total_files = len(list(Path(trim_dir).rglob("*.jpg")))
deletion_coefficient = maximum_no_of_files / total_files
print(f'Total files:{total_files}, deletion_coefficient = {deletion_coefficient}')

for root, subdirs, files in os.walk(trim_dir):
	for subdir in subdirs:
		print(os.path.join(root, subdir))
		os.chdir(os.path.join(root, subdir))
		folder_jpgs = glob.glob("*.jpg")
		if len(folder_jpgs) > minimum_number_of_files_to_be_trimmed:
			no_of_files_to_delete = len(folder_jpgs) - int(len(folder_jpgs) * deletion_coefficient)
			print(f'files:{len(folder_jpgs)}, files to delete:{no_of_files_to_delete}')
			for file in random.sample(folder_jpgs, no_of_files_to_delete):
				os.remove(file)

input("DONE")