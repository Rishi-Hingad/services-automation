import frappe

def execute():
    try:
        base_cols = [f.fieldname for f in frappe.get_meta('Account Master').fields]
        service_cols = [f.fieldname for f in frappe.get_meta('Service Account Master').fields]
        print(f"Base cols: {base_cols}")
        print(f"Service cols: {service_cols}")
        
        fields_to_migrate = [f for f in service_cols if f in base_cols and f != 'account_master']
        print(f"Fields to migrate: {fields_to_migrate}")
    except Exception as e:
        print(f"Error - {e}")
