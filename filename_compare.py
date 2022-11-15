import os

get_coords = lambda name: '_'.join(name.split('_')[-2:])


def filename_compare(base_dir, extension=None):
	# walk files and store their names, then list them sorted alphabetically
	has_extension = extension is not None
	end = f'.{extension}' if has_extension else '.'
	for dirpath, _, files in os.walk(base_dir):
		file_names = []
		for file_name in files:
			stat = os.stat(os.path.join(dirpath, file_name))
			modified_time = stat.st_mtime
			if not has_extension or file_name.endswith(end):
				file_name_truncated = file_name[0:file_name.index(end)]
				file_names.append({
					'modified_time': modified_time,
					'name': file_name_truncated,
				})
		sorted_file_names = list(
			map(lambda n: n['name'],
			sorted(file_names, key=lambda n: n['modified_time'])))

		files_to_check = []
		for i, file_name in enumerate(sorted_file_names):
			if get_coords(file_name) == get_coords(sorted_file_names[i - 1]):
				files_to_check.append(file_name)

		return '\n'.join(files_to_check)


# change these parameters as needed
print(filename_compare('/Users/dmayna/Documents/CityFramer/Maps', 'png'))
