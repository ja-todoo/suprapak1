from odoo import fields, models, api

class mrp(models.Model):

    _inherit = 'mrp.workcenter'
    _description = 'cambios en crentros de trabajo'

    costo_1 = fields.Float(string="Cost per hour")

    costo_2 = fields.Float(string="Cost per hour")