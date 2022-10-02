import string
from odoo.exceptions import ValidationError
from odoo import fields,api,models

class Level(models.Model):
    _name = 'level.emp'
    _description = 'kpi levels'

    name = fields.Char(string="Level Name",  required=True)
    level_from = fields.Float(string="Value From", required=True)
    level_to = fields.Float(string="Value To", required=True)

    @api.constrains('level_from','level_to')
    def check_kpi_level_overlap(self):
        for rec in self:
            if self.env['level.emp'].search([('id','!=',rec.id),('level_from','<=',rec.level_from),('level_to','>=',rec.level_from)]):
                raise ValidationError('Overlap')
            if self.env['level.emp'].search([('id','!=',rec.id),('level_from','<=',rec.level_to),('level_to','>=',rec.level_to)]):
                raise ValidationError('Overlap')
    @api.constrains('level_to','level_from')
    def check(self):
        for rec in self:
            if rec.level_to >100 or rec.level_to <=0:
                raise ValidationError("Can not be more than 100 or less than and eual to 0")
            elif rec.level_from <=0 or rec.level_from >100:
                raise ValidationError("Can not be less than 0 or more than 100")            

class kpi(models.Model):
    _name='emp.kpi'
    _description='empolyee kpi'
    month = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12')])
    year = fields.Selection([('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'),('2026','2026'),('2027','2027'),('2028','2028'),('2029','2029'),])
    quarter = fields.Selection([('1','Q1'),('2','Q2'),('3','Q3'),('4','Q4')])
    kpi = fields.Float()
    level = fields.Many2one('level.emp', compute="_compute_level")
    empolyee_id = fields.Many2one('hr.employee')

    @api.depends('kpi')
    def _compute_level(self):
        for rec in self:
            if rec:
                level = self.env['level.emp'].search([('level_from','<=',rec.kpi),('level_to','>=',rec.kpi)])
                print(level)
                print(rec.kpi)
                if len(level):
                    rec.level = level.id
                else:
                    rec.level = False
            else:
                rec.level = False
    @api.constrains('kpi')
    def check(self):
        for rec in self:
            if rec.kpi >100:
                raise ValidationError("Can not be more than 100")
            elif rec.kpi <=0:
                raise ValidationError("Can not be less than 0")

class Employee(models.Model):
    _inherit = 'hr.employee'
    emp_kpi_line = fields.One2many('emp.kpi', 'empolyee_id')
    type = fields.Selection([('quarter','Quarter'),('month','Month'),])