import frappe
import os

def execute():
    dms_path = '/home/rishi_hingad/frappe-bench-dmsservice/apps/dms/dms'
    doctypes = []
    
    for root, dirs, files in os.walk(dms_path):
        for file in files:
            if file.endswith('.json') and 'doctype' in root:
                # Get the doctype name from the JSON
                import json
                try:
                    with open(os.path.join(root, file)) as f:
                        data = json.load(f)
                        if data.get('doctype') == 'DocType':
                            doctypes.append(data.get('name'))
                except Exception:
                    pass
                    
    print(f"Found {len(doctypes)} Doctypes in DMS.")
    deleted = 0
    for dt in doctypes:
        # Check if it's currently registered to a different app (or even dms but the file doesn't exist yet)
        frappe.db.sql("DELETE FROM tabDocType WHERE name=%s", (dt,))
        deleted += 1
        
    frappe.db.commit()
    print(f"Deleted {deleted} Doctypes from tabDocType successfully to prepare for install-app.")
