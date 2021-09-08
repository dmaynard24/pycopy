import os


def file_delete(base_dir, filename_to_delete):
	for root, _, files in os.walk(base_dir):
		for file in files:
			if file == filename_to_delete:
				os.remove(os.path.join(root, file))


# change these parameters as needed
file_delete('/Users/dmayna/repos/side/project-euler/python/', '__init__.py')