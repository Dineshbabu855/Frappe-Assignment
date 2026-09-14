# Copyright (c) 2026, Dinesh  and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MYREP(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		ammount: DF.Int
		customer: DF.Data | None
		posting_date: DF.Date | None
	# end: auto-generated types

	pass
