# -*- coding: utf-8 -*-
# (c) 2016 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    attached = fields.Boolean(string='Attached', default=False)
