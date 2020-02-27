from odoo import models,fields,api

class SaleTaxes(models.Model):
    _inherit = 'sale.order.line'
    _description = 'amount sum tax'

    price = fields.Float('Subtotal',compute='calculo_amount')

    def calculo_amount(self):
        if self.price_tax:
            self.price = self.price + self.price_tax