import unittest
from odoo.tests import common
from io import BytesIO
import base64
import os


class TestExcelParsing(common.TransactionCase):

    def test_import_products_from_xlsx_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'products_data.xlsx')
        with open(file_path, 'rb') as file:
            excel_content = file.read()

        encoded_excel_file = base64.b64encode(excel_content)

        # Create a location record
        location_id = self.env['stock.location'].create({
            'name': 'Test Location',
            'usage': 'internal'
        })

        # Create a wizard instance with a valid location_id
        wizard = self.env['product.template.xlsx.wizard'].create({
            'xlsx_file': encoded_excel_file,
            'file_name': 'products_data.xlsx',
            'location_id': location_id.id
        })

        # Call the import function
        wizard.import_products_from_xlsx_file()

        self.assertTrue(self.env['product.template'].search([('name', '=', 'Samsung SM-A057 Galaxy')]))
        self.assertTrue(self.env['product.template'].search([('name', '=', 'Motorola Moto E13 Cosmic')]))
        self.assertTrue(self.env['product.template'].search([('name', '=', 'GARMIN Drive 55 MT-S Europe')]))
        self.assertTrue(self.env['product.template'].search([('name', '=', 'Chandelier LED-1003')]))
        self.assertTrue(self.env['product.template'].search([('name', '=', 'Lightbulb MK-300')]))


if __name__ == '__main__':
    unittest.main()
