from odoo import models,fields,api

class SaleTaxes(models.Model):
    _inherit = 'sale.order'
    _description = 'amount sum tax'

    def calculo_amount(self):
    
        if self.price_tax:
            self.subtotal_with_tax = float(self.price_subtotal) + self.price_tax

    subtotal_with_tax = fields.Float('Subtotal',compute='calculo_amount')

