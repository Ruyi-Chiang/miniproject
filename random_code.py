import os
import random

def rename_files(path):
	# get a list of file names from a folder
	os.chdir(path)
	file_list = os.listdir(path)
	print file_list
	# for each file, rename filename
	for file_name in file_list:
		random_int = str(random.randint(232, 2398))
		new_file_name = random_int + file_name + random_int
		os.rename(file_name, new_file_name)


rename_files("/Users/ruyi/Udacity_HW/mini_project/alphabet")