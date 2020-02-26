import os

# change these parameters as needed
base_dir = 'C:\\repos\\touchless-scaling\\src\\assets\\font\\Helvetica Now'
find_str = 'W05'
replace_str = ''

import os

# walk files and rename them
for root, dirs, files in os.walk(base_dir):
	for file_name in files:
		new_name = file_name.replace(find_str, replace_str)
		os.rename(root + '\\' + file_name, root + '\\' + new_name)