{
    'name': 'Hotel Management System',
    'version': '1.0',
    'summary': 'Module quản lý khách sạn và đặt phòng',
    'description': """
        Module quản lý khách sạn, phòng, đặc điểm phòng và đơn đặt phòng:
        - Quản lý khách sạn và danh sách phòng
        - Quản lý đặc điểm của phòng
        - Quản lý đơn đặt phòng
    """,
    'author': 'Duong Tu',
    'website': 'https://yourwebsite.com',
    'category': 'Management',
    'depends': ['base'],  
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'security/reacord_rule.xml',
        'views/hotel_view.xml',  # Views cho khách sạn
        'views/room_view.xml',  # Views cho phòng
        'views/room_feature.xml',  # Views cho đặc điểm phòng
        'views/bill_view.xml',  # Views cho đơn đặt phòng
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',  
}