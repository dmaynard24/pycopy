import os

# change these parameters as needed
base_dir = 'C:\\repos\\sazerac-aem-global\\ui.apps\\src\\main\\content\\jcr_root\\apps\\global\\components\\content\\'
file_to_read = '\\_cq_htmlTag\\.content.xml'
find_str = 'pagegrid '

# find and replace
child_directories = os.listdir(base_dir)
for cd in child_directories:
	# change this parameter as needed
	replace_str = cd + ' '
	with open(base_dir + cd + file_to_read) as f:
		s = f.read()
	s = s.replace(find_str, replace_str)
	with open(base_dir + cd + file_to_read, 'w') as f:
		f.write(s)
