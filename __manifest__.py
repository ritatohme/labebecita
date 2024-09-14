
{
    'name': 'Partner Gender Field',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Adds a gender field to res.partner',
    'description': 'This module adds a gender field to the res.partner model.',
    'depends': ['base'],
    'data': [
        'views/partner_view.xml',
    ],
    'installable': True,
    'application': False,
}
