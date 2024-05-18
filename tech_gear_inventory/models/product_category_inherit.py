# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = "product.category"

    description = fields.Text(string="Description")
