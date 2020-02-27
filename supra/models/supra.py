from odoo import models, fields , api

class Terminaciones(models.Model):
    _name = 'causales'
    _description = 'Causales terminación de contrato'

    name = fields.Char('causales de finalización de contrato')

class TerminacionesContrato(models.Model):
    _inherit = 'hr.contract'
    _description = 'Causales terminación de contratos'

    Causales = fields.Many2one('causales',string="Causales terminación de contrato")

