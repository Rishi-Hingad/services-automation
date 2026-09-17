import frappe

def execute():
    tables_to_drop = [
        "tabProduct Master", "tabAccount Master", "tabDistributor Master", "tabCountry Master",
        "tabCity Master", "tabDistrict Master", "tabPincode Master", "tabState Master", "tabZone Master",
        "tabProduct Category Master", "tabProduct Group Master"
    ]
    
    for table in tables_to_drop:
        if frappe.db.table_exists(table):
            frappe.db.sql(f"DROP TABLE `{table}`")
            print(f"Dropped {table}")
        else:
            print(f"{table} doesn't exist.")
    
    frappe.db.commit()
