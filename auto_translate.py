from openpyxl import load_workbook
import html

# defaults
default_categories = 'CCFE,FOS'
default_language = 'en_US'
default_protected = 'false'
xl_dir = 'C:\\Users\\dmayna\\Desktop\\CareerChoice\\Stories\\US8300\\Final content\\'
# always open the "master", this will hold custom label names
master_wb = load_workbook(
	filename=f'{xl_dir}Copy of App Flow Content FINAL, ENG - USA.xlsx')
filenames = {
	'fr_CA': 'Copy of App Flow Content FINAL, FR - CAN',
	'cs': 'Copy of App Flow Content FINAL, CZ -Czechia',
	'de': 'Copy of App Flow Content FINAL, DE_Germany',
	'es': 'Copy of App Flow Content FINAL, ES - ES',
	'fr': 'Copy of App Flow Content FINAL, FR - FR',
	'it': 'Copy of App Flow Content FINAL, IT',
	'pl': 'Copy of App Flow Content FINAL, POL',
	'sk': 'Copy of App Flow Content FINAL, SK',
	'es_CR': 'Copy of App Flow Content FINAL, ES - CRI',
}
sheet_name = '05 Academic Program'
wb_sheet_master = master_wb[sheet_name]
last_row_num = wb_sheet_master.max_row  # last row with content


def write_xml(out_dir, filename, xml, root_node):
	prefix = f'<?xml version="1.0" encoding="UTF-8"?>\n<{root_node} xmlns="http://soap.sforce.com/2006/04/metadata">\n'
	postfix = f'\n</{root_node}>'
	xml = f'{prefix}{xml.rstrip()}{postfix}'
	xml_file = f'{out_dir}{filename}'
	with open(xml_file, 'w', encoding='utf-8') as f:
		f.write(xml)


def write_custom_labels():
	# read master workbook, write to file
	xml = ''
	for i in range(1, last_row_num):
		label = wb_sheet_master[f'A{i + 1}'].value
		name = wb_sheet_master[f'B{i + 1}'].value
		if label is None or label.strip() == '' or name is None or name.strip(
		) == '':
			# empty cell
			continue
		label = html.escape(label)
		xml += f'\t<labels>\n\t\t<fullName>{name}</fullName>'
		xml += f'\n\t\t<categories>{default_categories}</categories>'
		xml += f'\n\t\t<language>{default_language}</language>'
		xml += f'\n\t\t<protected>{default_protected}</protected>'
		xml += f'\n\t\t<shortDescription>{name}</shortDescription>'
		xml += f'\n\t\t<value>{label}</value>'
		xml += f'\n\t</labels>\n'
	out_dir = 'C:\\repos\\ccnextgen-sfdx\\force-app\\main\\default\\labels\\'
	filename = 'CustomLabels.labels-meta.xml'
	write_xml(out_dir, filename, xml, 'CustomLabels')


def write_translations():
	# read all translation workbooks, write their contents to files
	for lang in filenames.keys():
		xml = ''
		wb_filename = filenames[lang]
		wb = load_workbook(filename=f'{xl_dir}{wb_filename}.xlsx')
		# go over all rows and create XML nodes for each lang
		wb_sheet = wb[sheet_name]
		for i in range(1, last_row_num):
			label = wb_sheet[f'A{i + 1}'].value
			name = wb_sheet_master[f'B{i + 1}'].value
			if label is None or label.strip() == '' or name is None or name.strip(
			) == '':
				# empty cell
				continue
			label = html.escape(label)
			xml += f'\t<customLabels>\n\t\t<label>{label}</label>\n\t\t<name>{name}</name>\n\t</customLabels>\n'
		out_dir = 'C:\\repos\\ccnextgen-sfdx\\force-app\\main\\default\\translations\\'
		filename = f'{lang}.translation-meta.xml'
		write_xml(out_dir, filename, xml, 'Translations')


write_custom_labels()
write_translations()
print('Done!')