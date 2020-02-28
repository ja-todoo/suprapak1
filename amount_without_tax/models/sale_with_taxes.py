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


class InvoiceTaxes(models.Model):
    _inherit = 'account.move.line'

    price_tax = fields.Float(compute='_compute_amount', string='Total Tax', readonly=True, store=True)
    price_with_tax = fields.Float(compute='_compute_amount', string='Total With Tax', readonly=True, store=True)

    @api.depends('quantity', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.quantity, product=line.product_id, partner=line.order_id.partner_shipping_id)
            price_tax = sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
            price_with_tax = line.price_subtotal + price_tax
            line.update({
                'price_tax': price_tax,
                'price_with_tax': price_with_tax,
            })
    

