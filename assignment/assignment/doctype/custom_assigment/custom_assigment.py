# Copyright (c) 2026, Dinesh  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CustomAssigment(Document):
	def validate(self):
		if not self.description:
			self.description = "No description provided."
def executePrint(doc, method):
	frappe.msgprint("Print executed successfully.")
