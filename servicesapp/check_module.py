import frappe

def execute():
    app = frappe.local.module_app.get('masters')
    print("Module masters points to app:", app)
