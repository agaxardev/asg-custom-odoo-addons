{
    'name': "hr_contract_extended",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
Long description of module's purpose.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base','hr','hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_extended_views.xml',
    ],
    'installable': True,
    'application': True,
}
