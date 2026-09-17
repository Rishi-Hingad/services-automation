import frappe

def execute():
    modules = ['Approval', 'Masters']
    for m in modules:
        if frappe.db.exists("Module Def", m):
            frappe.db.set_value("Module Def", m, "app_name", "dms")
            print(f"Updated Module {m} app_name to dms")
            
    # Also delete Doc Approval from tabDocType just in case
    frappe.db.sql("DELETE FROM tabDocType WHERE name='Doc Approval'")
    print("Deleted Doc Approval from tabDocType")
    
    frappe.db.commit()
