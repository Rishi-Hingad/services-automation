import frappe

def execute():
    val = frappe.db.get_value("Module Def", "Approval", "app_name")
    print(f"Approval module app_name: {val}")
