from odoo import fields, models, api

class ContractCristian(models.Model):

    _inherit = 'hr'#.contract'
    _description = 'Campos nuevos para el contrato'

    ARL = fields.Many2one('res.partner')

    EPS = fields.Many2one('res.partner')

    Pension = fields.Many2one('res.partner',string="Pensión")

    Cesantias = fields.Many2one('res.partner')

    Caja = fields.Many2one('res.partner', string="Caja de compensación familiar")

    