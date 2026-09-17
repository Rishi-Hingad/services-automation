import frappe

def execute():
    for dt in ['Account Master', 'Product Master', 'Distributor Master']:
        try:
            count = frappe.db.sql(f"SELECT COUNT(*) FROM `tab{dt}`")[0][0]
            print(f"{dt}: {count}")
        except Exception as e:
            print(f"{dt}: Error - {e}")
