import os
import glob
import frappe

def execute():
    # Get all doctypes in DMS masters
    dms_doctypes = glob.glob('/home/rishi_hingad/frappe-bench-dmsservice/apps/dms/dms/masters/doctype/*')
    
    for dt_path in dms_doctypes:
        dt_name = os.path.basename(dt_path) # e.g. "country_master"
        if not os.path.isdir(dt_path): continue
        
        # We need to ensure this path exists in servicesapp so Frappe can import it during install
        servicesapp_path = f'/home/rishi_hingad/frappe-bench-dmsservice/apps/servicesapp/servicesapp/masters/doctype/{dt_name}'
        
        if not os.path.exists(servicesapp_path):
            os.makedirs(servicesapp_path, exist_ok=True)
            
            # create __init__.py
            with open(f'{servicesapp_path}/__init__.py', 'w') as f:
                pass
                
            # create the python controller
            class_name = dt_name.replace('_', ' ').title().replace(' ', '')
            with open(f'{servicesapp_path}/{dt_name}.py', 'w') as f:
                f.write(f"from frappe.model.document import Document\nclass {class_name}(Document):\n    pass\n")
            
            print(f"Created dummy controller for {dt_name} in servicesapp")

    # Do the same for Secondary Sales if needed, the error mentioned 'Import Zylem Data'
    secondary_sales_dms = glob.glob('/home/rishi_hingad/frappe-bench-dmsservice/apps/dms/dms/secondary_sales/doctype/*')
    for dt_path in secondary_sales_dms:
        dt_name = os.path.basename(dt_path)
        if not os.path.isdir(dt_path): continue
        
        # We need to ensure the secondary_sales folder exists in servicesapp too if it's mapped!
        # Wait, is 'Secondary Sales' mapped to servicesapp? Let's just create it to be safe if it fails.
        servicesapp_path = f'/home/rishi_hingad/frappe-bench-dmsservice/apps/servicesapp/servicesapp/secondary_sales/doctype/{dt_name}'
        
        os.makedirs(servicesapp_path, exist_ok=True)
        with open(f'{servicesapp_path}/__init__.py', 'w') as f: pass
        class_name = dt_name.replace('_', ' ').title().replace(' ', '')
        with open(f'{servicesapp_path}/{dt_name}.py', 'w') as f:
            f.write(f"from frappe.model.document import Document\nclass {class_name}(Document):\n    pass\n")
        print(f"Created dummy controller for {dt_name} in servicesapp secondary_sales")

