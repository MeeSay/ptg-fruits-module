from odoo import models, fields

class PtgFruit(models.Model):
    _name = 'ptg.fruit'
    _description = 'PTG Fruit'

    name = fields.Char(string='Fruit Name', required=True)
    average = fields.Float(string='Average', required=False, digits=(16, 6))
    imgs = fields.Char(string='Fruit Image')
