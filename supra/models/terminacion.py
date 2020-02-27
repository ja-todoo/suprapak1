from odoo import fields, models

class TerminacionesContrato(models.Model):
    _inherit = 'hr.contract'
    _description = 'Causales terminación de contratos'

    Causales = fields.Many2one('causales',string="Causales terminación de contrato")