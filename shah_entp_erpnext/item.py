from __future__ import unicode_literals

def set_item_code(doc, method):
	if not doc.item_code:
		doc.item_code = doc.cas_no or doc.mdl_no
