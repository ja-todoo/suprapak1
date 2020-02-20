from odoo import fields, models, api

class mrpjulian(models.Model):

    _inherit = 'mrp.workcenter'
    _description = 'cambios en crentros de trabajo'

    costo_1 = fields.Float(string="Cost per hour")
    analityc_count = fields.Many2one('account.analytic.account',string="Analytic Account")
    costo_2 = fields.Float(string="Cost per hour")
    analityc_count2 = fields.Many2one('account.analytic.account',string="Analytic Account")