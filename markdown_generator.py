import os


def generate_table(project_name, base_js_dir, base_python_dir,
	question_link_prefix, github_link_prefix):
	def body_line_from_path(js_path, python_path):
		question_num_index = js_path.index('.js')
		question_num = int(js_path[question_num_index - 3:question_num_index])
		shortened_js_path = js_path[js_path.index('javascript'):]
		shortened_python_path = python_path[python_path.index('python'):]
		return f'| [Question #{question_num}]({question_link_prefix}{question_num}) | [JavaScript]({github_link_prefix}{shortened_js_path}) | [Python]({github_link_prefix}{shortened_python_path}) |'

	def get_python_paths_dict_from_js_paths(js_file_paths):
		python_paths = {}
		for path in js_file_paths:
			beg = path[:path.index('questions')]
			mid = path[path.index('questions'):path.rindex('/question')].replace(
				'-', '_')
			python_path = (beg + mid).replace('javascript', 'python')
			python_paths[python_path] = 1
		return python_paths

	# read javascript filenames
	js_file_paths = []
	for root, _, files in os.walk(base_js_dir):
		for file in files:
			if file.find('question') > -1 and not file.endswith('.test.js'):
				js_file_paths.append(os.path.join(root, file))

	# read python filenames
	python_paths_dict = get_python_paths_dict_from_js_paths(js_file_paths)
	python_file_paths = []
	for root, _, files in os.walk(base_python_dir):
		for file in files:
			if root in python_paths_dict and file != '__init__.py' and not file.endswith(
				'_test.py'):
				with open(os.path.join(root, file)) as f:
					try:
						first_char = f.read(1)
						if first_char == '#':
							python_file_paths.append(os.path.join(root, file))
					except UnicodeDecodeError:
						continue

	# beginning string generation
	head_lines = [
		f'| {project_name} Question | JavaScript Solution | Python Solution |',
		'| - | - | - |'
	]
	body_lines = list(
		map(body_line_from_path, sorted(js_file_paths), sorted(python_file_paths)))

	return '\n'.join(head_lines + body_lines)


print(
	generate_table(
	'Project Euler',
	'/Users/dmayna/repos/side/project-euler/javascript/questions-001-100',
	'/Users/dmayna/repos/side/project-euler/python/questions_001_100',
	'https://projecteuler.net/problem=',
	'https://github.com/dmaynard24/project-euler/blob/master/'))
