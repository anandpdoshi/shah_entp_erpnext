from __future__ import unicode_literals
import frappe
import json
from frappe.utils import strip, cstr

products_json = '/Users/anandpdoshi/Dropbox/Design/Work/shah-enterprises/products/products.json'
impurities_json = '/Users/anandpdoshi/Dropbox/Design/Work/shah-enterprises/impurities/impurities.json'

def execute():
	import_json(products_json, defaults={
		'item_group': 'Products',
		'show_in_website': 1,
		'default_warehouse': 'Stores - SE'
	})
	import_json(impurities_json, defaults={
		'item_group': 'Impurities',
		'show_in_website': 1,
		'default_warehouse': 'Stores - SE'
	})

def import_json(file, defaults):
	with open(file, 'r') as f:
		data = json.loads(f.read())

	could_not_create = []
	try:
		for i, d in enumerate(data):
			try:
				import_doc(d, defaults)
				frappe.db.commit()

			except Exception, e:
				frappe.db.rollback()
				could_not_create.append(d)

				if 'Item Code is mandatory' in cstr(e):
					pass

				else:
					print frappe.get_traceback()

	finally:

		print '-'*80
		print file
		print frappe.as_json(could_not_create)

def import_doc(d, defaults):
	doc = frappe.new_doc('Item')

	doc.cas_no = d.get('cas_no')
	doc.mdl_no = d.get('mdl_no')

	if doc.cas_no == 'NA':
		doc.cas_no = None

	if doc.mdl_no == 'NA':
		doc.mdl_no = None

	doc.description = d.get('description')
	if 'Synonym:' in doc.description:
		description = doc.description.split('Synonym:')
		doc.item_name = strip(description[1])
		doc.description = strip(description[0]) + '\nSynonym: ' + doc.item_name

		if not (doc.cas_no and doc.mdl_no):
			# use synonym as item code for now
			doc.item_code = doc.item_name

	else:
		doc.item_name = doc.description

	doc.update(defaults)
	doc.insert()

	if d.get('image'):
		file_url = '/files/{0}'.format(d['image'])

		# attach image
		frappe.get_doc({
			"doctype": "File",
			"file_url": file_url,
			"attached_to_doctype": "Item",
			"attached_to_name": doc.name
		}).insert()

		doc.image = file_url
		doc.save()

	# print doc.as_json()
