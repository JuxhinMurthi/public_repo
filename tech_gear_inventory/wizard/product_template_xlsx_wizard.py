# -*- coding: utf-8 -*-
import datetime
from odoo import fields, models, api, _
from odoo.exceptions import UserError
import io
import base64
import pandas as pd


class ProductTemplateXlsxWizard(models.TransientModel):
    _name = "product.template.xlsx.wizard"
    _description = "Transient model used for importing products from an xlsx file"

    parent_category_id = fields.Many2one("product.category", string="Parent Product Category")
    location_id = fields.Many2one('stock.location', string='Product Storage Location', required=True)
    xlsx_file = fields.Binary(string="Upload Excel File", required=True)
    file_name = fields.Char(string="File Name")

    def import_products_from_xlsx_file(self):
        self.ensure_one()
        if not self.xlsx_file or not self.file_name.endswith(".xlsx"):
            raise UserError(_("Please upload a valid .xlsx Excel file."))

        file_content = base64.b64decode(self.xlsx_file)

        try:
            df = pd.read_excel(io.BytesIO(file_content))

            for index, row in df.iterrows():
                product_name = row["Product Name"]
                product_category = row["Category"]
                product_price = row["Price"]
                product_quantity = row["Quantity"]

                # Check if the product category exists, if not create a new one
                category_id = self.env["product.category"].search([("name", "=", product_category)])
                if not category_id:
                    category_id = self.env["product.category"].create({
                        "name": product_category,
                        "parent_id": self.parent_category_id.id if self.parent_category_id else None
                    })

                # Check if the product exists, if not create a new one, if yes update the product
                product = self.env["product.template"].search([("name", "=", product_name)])
                if not product:
                    product = self.env["product.template"].create({
                        "name": product_name,
                        "categ_id": category_id.id,
                        "list_price": product_price,
                        "type": "product",
                    })
                else:
                    product.write({
                        "categ_id": category_id.id,
                        "list_price": product_price,
                        "type": "product",
                    })

                # Create a stock quant to add new quantity to the product if it doesn't exist
                # if it does, update quantity
                product_product = product.product_variant_id

                quant = self.env['stock.quant'].search([
                    ('product_id', '=', product_product.id),
                    ('location_id', '=', self.location_id.id)
                ])
                if quant:
                    quant.write({
                        'inventory_quantity': quant.quantity + product_quantity,
                        'inventory_date': datetime.date.today()
                    })
                else:
                    self.env['stock.quant'].create({
                        'product_id': product_product.id,
                        'location_id': self.location_id.id,
                        'quantity': product_quantity,
                        'inventory_quantity': product_quantity,
                        'inventory_date': datetime.date.today()
                    })

        except Exception as e:
            raise UserError(_("Error processing the Excel file: %s") % str(e))

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
