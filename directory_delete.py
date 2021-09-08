import os, shutil


def directory_delete(base_dir, dirname_to_delete):
	for root, dirs, _ in os.walk(base_dir):
		for dir in dirs:
			if dir == dirname_to_delete:
				shutil.rmtree(os.path.join(root, dir))


# change these parameters as needed
directory_delete('/Users/dmayna/repos/side/project-euler/python/',
	'__pycache__')
