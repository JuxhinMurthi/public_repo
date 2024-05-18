{
    "name": "Tech Gear Inventory",
    "description": "Custom module for extending Inventory Module Functionality",
    "author": "Juxhin Murthi",
    "category": "Inventory",
    "sequence": 100,
    "depends": [
        "base",
        "product",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_category_views_inherit.xml",
        "views/product_template_views_inherit.xml",
        "wizard/product_template_xlsx_wizard_view.xml",
    ],
    "demo": [

    ],
    'assets': {
       'web.assets_backend': [
           '/tech_gear_inventory/static/src/js/product_template_list_button.js',
           '/tech_gear_inventory/static/src/js/product_template_kanban_button.js',
           '/tech_gear_inventory/static/src/xml/product_template_list_button.xml',
           '/tech_gear_inventory/static/src/xml/product_template_kanban_button.xml'
       ]
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    'license': 'LGPL-3',
}