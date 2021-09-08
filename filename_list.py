import os


def filename_list(base_dir, extension=None):
	# walk files and store their names, then list them sorted alphabetically
	has_extension = extension is not None
	end = f'.{extension}' if has_extension else '.'
	for _, _, files in os.walk(base_dir):
		file_names = []
		for file_name in files:
			if not has_extension or file_name.endswith(end):
				file_names.append(file_name[0:file_name.index(end)])
		return '\n'.join(sorted(set(file_names)))


# change these parameters as needed
print(
	filename_list(
	'/Users/dmayna/workplace/EMCEditorNodeJS-workspace/src/NodeJS-EMCManager/src/Experiment/components',
	'tsx'))
