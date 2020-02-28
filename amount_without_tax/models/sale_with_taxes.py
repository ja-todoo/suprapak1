from odoo import models,fields,api

class SaleTaxes(models.Model):
    _inherit = 'Sales Order Line'
    _description = 'amount sum tax'

    precio = float(self.price_subtotal)

    def calculo_amount(self):
        if self.price_tax:
            self.price = self.precio + self.price_tax

    x_studio_subtotal_with_tax = fields.Float('Subtotal',compute='calculo_amount')

