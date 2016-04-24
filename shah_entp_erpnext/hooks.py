# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "shah_entp_erpnext"
app_title = "Shah Enterprises ERPNext Extension"
app_publisher = "Anand Doshi"
app_description = "Shah Enterprises ERPNext Extension"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "anand@erpnext.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shah_entp_erpnext/css/shah_entp_erpnext.css"
# app_include_js = "/assets/shah_entp_erpnext/js/shah_entp_erpnext.js"

# include js, css files in header of web template
web_include_css = [
	"/assets/shah_entp_erpnext/css/website.css",
	# "/assets/shah_entp_erpnext/fonts/leaguespartan/stylesheet.css",
]
# web_include_js = "/assets/shah_entp_erpnext/js/shah_entp_erpnext.js"

website_context = {
	'hide_login': 1
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "shah_entp_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "shah_entp_erpnext.install.before_install"
# after_install = "shah_entp_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shah_entp_erpnext.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Fixtures
# --------
fixtures = ["Custom Field"]

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"before_insert": "shah_entp_erpnext.item.set_item_code"
	}
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shah_entp_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"shah_entp_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"shah_entp_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shah_entp_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"shah_entp_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "shah_entp_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shah_entp_erpnext.event.get_events"
# }

