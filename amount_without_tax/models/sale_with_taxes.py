from odoo import models,fields,api

class SaleTaxes(models.Model):
    _inherit = 'Sales Order Line'
    _description = 'amount sum tax'

    def calculo_amount(self):
    
        if self.price_tax:
            self.price = float(self.price_subtotal) + self.price_tax

    subtotal_with_tax = fields.Float('Subtotal',compute='calculo_amount')

