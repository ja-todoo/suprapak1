from odoo import models,fields,api

class SaleTaxes(models.Model):
    _inherit = 'sale.order.line'
    _description = 'amount sum tax'

    def calculo_amount(self):
    
        for record in self:
            if record.price_tax:
                record.subtotal_with_tax = record.price_subtotal + record.price_tax
            else:
                record.subtotal_with_tax = record.price_subtotal
        

    subtotal_with_tax = fields.Float('Subtotal',compute='calculo_amount')

