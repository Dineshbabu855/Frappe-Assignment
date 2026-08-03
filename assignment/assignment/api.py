import frappe
from frappe.query_builder import DocType


@frappe.whitelist()
def api_whitelist_demo():

    Parent = DocType("ApiWhitelist")
    Child = DocType("whitelistchild")

    records = (
        frappe.qb.from_(Parent)
        .join(Child)
        .on(Child.parent == Parent.name)
        .select(
            Parent.name,
            Child.ro,
            Child.tow
        )
        .limit(10)
        .run(as_dict=True)
    )

    if not records:
        return []

    doc = frappe.get_doc("ApiWhitelist", records[0]["name"])

    doc.name1 = "Updated using Document API"
    doc.save()

    names = {row["name"] for row in records}

    for name in names:
        frappe.db.set_value(
            "ApiWhitelist",
            name,
            "name1",
            "Updated using Database API",
            update_modified=False
        )

    return records