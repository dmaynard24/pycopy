import os

# change these parameters as needed
base_dir = 'C:\\repos\\project-euler\\python'
find_str = '-'
replace_str = '_'

import os

# walk directories and rename them
for root, dirs, files in os.walk(base_dir):
	new_name = root.replace(find_str, replace_str)
	os.rename(root, new_name)