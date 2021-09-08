import os

# change these parameters as needed
base_dir = 'C:\\Users\\dmayna\\Desktop\\CareerChoice\\Stories\\7685'
find_str = 'Onsite'
replace_str = 'Online'

import os

# walk files and rename them
for root, _, files in os.walk(base_dir):
	for file_name in files:
		new_name = file_name.replace(find_str, replace_str)
		os.rename(root + '\\' + file_name, root + '\\' + new_name)