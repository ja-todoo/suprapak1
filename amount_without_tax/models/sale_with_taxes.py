from odoo import models,fields,api

class SaleTaxes(models.Model):
    _inherit = 'sale.order'
    _description = 'amount sum tax'

    price1 = fields.Float('Subtotal',compute='calculo_amount')

    def calculo_amount(self):
        if self.price_tax:
            self.price = self.price_subtotal + self.price_tax