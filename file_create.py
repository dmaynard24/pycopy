import os


def file_create(base_dir, filename, dirname_exception=None):
	# walk directories at the top level of the base directory
	for root, dirs, _ in os.walk(base_dir):
		for dir in dirs:
			# skip directories by name
			if dirname_exception is None or dir != dirname_exception:
				# write empty file
				with open(os.path.join(root, filename), 'w'):
					pass


# change these parameters as needed
file_create('/Users/dmayna/repos/side/project-euler/python/', '__init__.py',
	'__pycache__')
