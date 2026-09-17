import frappe

def execute():
    # 1. Map of complex doctypes and their new Service counterpart
    mapping = {
        'Account Master': 'Service Account Master',
        'Product Master': 'Service Product Master',
        'Distributor Master': 'Service Distributor Master'
    }

    print("Starting data migration for split Doctypes...")
    
    for base_dt, service_dt in mapping.items():
        base_table = f"tab{base_dt}"
        service_table = f"tab{service_dt}"
        
        # Check if the tables exist
        if not frappe.db.table_exists(base_dt):
            print(f"Base table {base_table} does not exist. Skipping.")
            continue
            
        if not frappe.db.table_exists(service_dt):
            print(f"Service table {service_table} does not exist. Did you run bench migrate?")
            continue
            
        # Get all unique fields in the service doctype (excluding standard ones)
        service_fields = [d.fieldname for d in frappe.get_meta(service_dt).fields]
        
        # We need to find which fields actually exist in the old table
        # Since we just dropped the JSON from servicesapp, the columns in base_table STILL exist!
        columns_in_base = frappe.db.sql(f"DESC `{base_table}`", as_dict=1)
        base_cols = [c.Field for c in columns_in_base]
        
        fields_to_migrate = [f for f in service_fields if f in base_cols and f != base_dt.lower().replace(' ', '_')]
            
        # Select all records from base_table
        select_cols = ['name'] + fields_to_migrate
        records = frappe.db.sql(f"SELECT * FROM `{base_table}`", as_dict=True)
        
        with open("/tmp/migration.log", "a") as f:
            f.write(f"Migrating {base_dt}... Found {len(records)} records.\n")
            f.write(f"Fields to migrate: {fields_to_migrate}\n")
        
        migrated_count = 0
        error_count = 0
        
        for base_data in records:
            base_name = base_data.get('name')
            # Check if service record already exists
            link_fieldname = base_dt.lower().replace(' ', '_')
            exists = frappe.db.exists(service_dt, {link_fieldname: base_name})
            if exists:
                continue
                
            try:
                new_doc = frappe.new_doc(service_dt)
                new_doc.set(link_fieldname, base_name)
                
                # Migrate matching fields if any exist
                fields_to_migrate = [f for f in service_fields if f in base_cols and f != link_fieldname]
                for field in fields_to_migrate:
                    new_doc.set(field, base_data.get(field))
                
                new_doc.insert(ignore_permissions=True, ignore_mandatory=True)
                migrated_count += 1
            except Exception as e:
                error_count += 1
                with open("/tmp/migration.log", "a") as f:
                    f.write(f"Error migrating {base_name} to {service_dt}: {str(e)}\n")
                
        with open("/tmp/migration.log", "a") as f:
            f.write(f"Successfully migrated {migrated_count} records for {service_dt}.\n")
        frappe.db.commit()

    print("Data migration completed successfully.")
