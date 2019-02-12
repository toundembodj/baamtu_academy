# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartnerExtension(models.Model):
    _inherit = 'res.partner'

    region = fields.Many2one("res.country", string="Région")