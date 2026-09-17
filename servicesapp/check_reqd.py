import frappe

def execute():
    try:
        service_cols = [f.fieldname for f in frappe.get_meta('Service Account Master').fields if f.reqd]
        print(f"Service Account Master mandatory cols: {service_cols}")
        
        service_cols = [f.fieldname for f in frappe.get_meta('Service Product Master').fields if f.reqd]
        print(f"Service Product Master mandatory cols: {service_cols}")

        service_cols = [f.fieldname for f in frappe.get_meta('Service Distributor Master').fields if f.reqd]
        print(f"Service Distributor Master mandatory cols: {service_cols}")

    except Exception as e:
        print(f"Error - {e}")
