from openerp import models
from openerp import fields
from openerp import api

class EntityType(models.Model):
        _name = 'softcoded_values.entity.type'
        
        name = fields.Char('Name', required=True)
        
        attribute_ids = fields.One2many('softcoded_values.attribute', 'entity_type_id', string='Attributes', required=True)
        
class Entity(models.Model):
        _name = 'softcoded_values.entity'
        
        entity_type_id = fields.Many2one('softcoded_values.entity.type', string='Entity Type', required=True)
        
        def read(self):
                #for attr in self.entity_type_id.attribute_ids:
                        
                return []
        
        def create(self):
                pass
        
class Attribute(models.Model):
        _name = 'softcoded_values.attribute'
        
        data_type = fields.Selection([
                                      ('integer', 'Integer'),
                                      ('decimal', 'Decimal'),
                                      ('string', 'String'),
                                      ('datetime', 'Datetime'),
                                      ('enum', 'Enum'),
                                      ], 'Data Type', required=True)
        max_length = fields.Integer('Max Length', required=True)
        min_multiplicity = fields.Integer('Min Multiplicity', required=True)
        max_multiplicity = fields.Integer('Max Multiplicity', required=True)
        entity_type_id = fields.Many2one('softcoded_values.entity.type', string='Entity Type', required=True)
        name = fields.Char('Attribute Name', required=True)
        sequence_number = fields.Integer('Sequence Number', required=True)
        
class EnumValue(models.Model):
        _name = 'softcoded_values.enum.value'
        
        attribute_id = fields.Many2one('softcoded_values.attribute', string='Attribute', required=True)
        value_integer = fields.Integer()
        value_decimal = fields.Float()
        value_string = fields.Char()
        value_datetime = fields.Datetime()
        
class SoftcodedValue(models.Model):
        _name = 'softcoded_values.softcoded.value'
        
        value_integer = fields.Integer()
        value_decimal = fields.Float()
        value_string = fields.Char()
        value_datetime = fields.Datetime()
        attribute_id = fields.Many2one('softcoded_values.attribute', required=True)
        entity_id = fields.Many2one('softcoded_values.entity', required=True)
        
#TEST Class
class Person(models.Model):
        _name = 'softcoded_values.entity'
        _inherit = 'softcoded_values.entity'
        
        entity_type_id = fields.Many2one(compute='get_entity_type', comodel_name='softcoded_values.entity.type')
        
        @api.one
        def get_entity_type(self):
                domain = [
                          ('name', '=', 'Person')
                          ]
                id_ = self.env['softcoded_values.entity.type'].search(self.env.cr, self.env.uid, domain)
                self.entity_type_id = id_