import frappe

def execute():
    # Find all doctypes in DMS that clash
    dms_doctypes = [
        "Product Master", "Account Master", "Distributor Master", "Country Master",
        "City Master", "District Master", "Pincode Master", "State Master", "Zone Master",
        "Product Category Master", "Product Group Master", "Import Zylem Data"
    ]
    
    # Delete them from tabDocType so install-app doesn't try to load their old python modules
    for dt in dms_doctypes:
        frappe.db.sql(f"DELETE FROM tabDocType WHERE name=%s", (dt,))
    
    frappe.db.commit()
    print("Deleted conflicting tabDocTypes successfully.")
