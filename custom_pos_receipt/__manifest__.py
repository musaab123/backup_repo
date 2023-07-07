
{
    'name': 'POS Custom Receipt',
    'category': 'Sales/Point of Sale',
    'description': "Customized our point of sale receipt",
    'version': '15.0.1.0',
    'website': 'https://www.kanakinfosystems.com',
    'author': 'Ziad ',
    'images': ['static/description/banner.jpg'],
    'depends': ['base', 'point_of_sale','l10n_sa_pos',],

    #  'data': [
    #     'views/data.xml',
    # ],
    'assets': {
        'point_of_sale.assets': [
            "custom_pos_receipt/static/src/xml/pos.xml",
            # "custom_pos_receipt/static/src/xml/pos_inh.xml",
        ],
       
        # 'point_of_sale.assets': [
        #     'custom_pos_receipt/static/src/js/models.js',
        # ],
   
        
        
    },
    'installable': True,
}
