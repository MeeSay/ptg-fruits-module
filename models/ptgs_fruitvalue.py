from odoo import models, fields

class PtgFruitValue(models.Model):
    _name = 'ptg.fruit.value'
    _description = 'PTG Fruit Value'

    fruit_name = fields.Many2one('ptg.fruit', string='Fruit Name', required=True)
    weight = fields.Float(string='Weight', required=True)
    value = fields.Float(string='Value (xu)', required=True)
    
