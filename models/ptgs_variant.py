from odoo import models, fields

class PtgVariant(models.Model):
    _name = 'ptg.variant'
    _description = 'PTG Variant'

    name = fields.Char(string='Variant', required=True)
    value = fields.Float(string='Value (x)', required=True, digits=(16, 6))
    text_color = fields.Char(string='Text Color', required=False)
    background_color = fields.Char(string='Background Color', required=False)
    
    # Required for inbound sync from external sources
    conversion_id = fields.Char(
        string="Source ID",
        help="Original ID from external source (Firebase/Firestore/MongoDB)",
        index=True,
        copy=False
    )
