import shutil, os


def copy_directory(src, dest):
	try:
		shutil.copytree(src, dest)
	# Directories are the same
	except shutil.Error as e:
		print('Directory not copied. Error: %s' % e)
	# Any error saying that the directory doesn't exist
	except OSError as e:
		print('Directory not copied. Error: %s' % e)


# change these parameters as needed
base_dir = 'C:\\repos\\sazerac-aem-global\\ui.apps\\src\\main\\content\\jcr_root\\apps\\global\\components\\content\\'
src_dir = 'C:\\repos\\sazerac-aem-global\\ui.apps\\src\\main\\content\\jcr_root\\apps\\global\\components\\content\\pagegrid\\_cq_htmlTag'
copy_dir = '\\_cq_htmlTag'

# copy
child_directories = os.listdir(base_dir)
for cd in child_directories:
	copy_directory(src_dir, base_dir + cd + copy_dir)
