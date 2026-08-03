# Copyright (c) 2026, Dinesh  and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ApiWhitelist(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from assignment.assignment.doctype.whitelistchild.whitelistchild import whitelistchild
		from frappe.types import DF

		name1: DF.Data | None
		table_adpz: DF.Table[whitelistchild]
	# end: auto-generated types

	pass
