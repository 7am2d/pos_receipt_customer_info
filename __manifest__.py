# -*- coding: utf-8 -*-
#################################################################################
# Author      : E-Corp.org. (<https://www.E-Corp.org/>)
# Copyright(c): 2012-Present E-Corp.org.
# All Rights Reserved.
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.E-Corp.org/license>
#################################################################################
{
    'name': 'POS Custom Information on Receipt',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'summary': 'This module is used to print receipt of point of sale when a user adds a product in the cart and validates payment and print receipt, then the user can see the client name on POS Receipt, Custom phone number, and Custom address',
    'website': 'www.E-Corp.org',
    'author': 'E-Corp.org',
    'images': ['static/description/banner.jpg'],
    'description': "Customized point of sale receipt with customer information easy to use",
    'depends': ['base', 'point_of_sale'],
    "data": [],
    'demo': [],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
}
