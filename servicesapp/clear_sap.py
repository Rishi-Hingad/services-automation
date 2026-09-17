import frappe

def execute():
    try:
        frappe.db.sql("DELETE FROM `tabSAP Field Mapper`")
        frappe.db.sql("DELETE FROM `tabSAP Parent Field Mapper Item`")
        frappe.db.sql("DELETE FROM `tabSAP Child Field Mapper Item`")
        frappe.db.commit()
        print("Cleared SAP Field Mapper tables")
    except Exception as e:
        print(f"Error: {e}")
