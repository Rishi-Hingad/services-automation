import frappe

def execute():
    try:
        print(f"table_exists(tabAccount Master): {frappe.db.table_exists('tabAccount Master')}")
        print(f"table_exists(Account Master): {frappe.db.table_exists('Account Master')}")
    except Exception as e:
        print(f"Error - {e}")
