from odoo import models, fields , api

class Terminaciones(models.Model):
    _name = 'causales'
    _description = 'Causales terminación de contrato'

    name = fields.Char('causales de finalización de contrato')

