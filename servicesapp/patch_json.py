import json
import frappe

def execute():
    path = '/home/rishi_hingad/frappe-bench-dmsservice/apps/dms/dms/masters/doctype/distributor_master/distributor_master.json'
    with open(path, 'r') as f:
        data = json.load(f)
        
    for field in data.get('fields', []):
        if field.get('fieldtype') == 'Data':
            if 'length' not in field:
                field['length'] = 50
                
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Updated distributor_master.json lengths!")
