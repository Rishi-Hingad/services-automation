import frappe

def execute():
    modules = frappe.db.sql("SELECT name, app_name FROM `tabModule Def` WHERE app_name='servicesapp'", as_dict=True)
    for m in modules:
        print(f"Module: {m.name}, App: {m.app_name}")
