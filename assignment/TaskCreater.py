import frappe

@frappe.whitelist()
def create_task(task_subject):
    doc = frappe.new_doc("Task")
    doc.subject = task_subject
    doc.save()

    return doc.name