from odoo import models, fields

class PtgVariant(models.Model):
    _name = 'ptg.variant'
    _description = 'PTG Variant'

    name = fields.Char(string='Variant', required=True)
    value = fields.Float(string='Value (x)', required=True)
    
