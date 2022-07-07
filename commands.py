
nav_map = {
    'posted_on_the_board': ['categories', 'on_board_new_ads', 'on_board_all_ads', 'back_to_start'],
    'outside_board': ['outside_board_new_ads', 'outside_board_all_ads', 'back_to_start'],
    'categories': ['vacancy', 'bid', 'call', 'other_ads', 'back_21'],
    'other_ads': ['missing', 'assistance', 'social', 'product', 'exhibition', 'lottery', 'educational', 'art', 'other', 'back_20'],
    'vacancy': ['new_vacancy', 'all_vacancy', 'back_5'],
    'bid': ['new_bid', 'all_bid', 'back_8'],
    'call': ['new_call', 'all_call', 'back_11'],
    'top_menu': ['posted_on_the_board', 'outside_board'],
    'stop': ['restart']
}


back_map = {
    'back_1': 'posted_on_the_board',
    'back_2': 'posted_on_the_board',
    'back_3': 'vacancy',
    'back_4': 'vacancy',
    'back_5': 'categories',
    'back_6': 'bid', 
    'back_7': 'bid',
    'back_8': 'categories',
    'back_9': 'call',
    'back_10': 'call',
    'back_11': 'categories',
    'back_12': 'other_ads', 
    'back_13': 'other_ads',
    'back_14': 'other_ads',
    'back_15': 'other_ads',
    'back_16': 'other_ads',
    'back_17': 'other_ads',
    'back_18': 'other_ads',
    'back_19': 'other_ads',
    'back_20': 'categories',
    'back_21': 'posted_on_the_board',
    'back_22': 'back_to_main',
    'back_23': 'outside_board',
    'back_24': 'outside_board',
    'back_25': 'other_ads',
    'back_to_start': 'top_menu'
}


sent_img_signals = {
    'missing': 'back_12',
    'assistance': 'back_13',
    'social': 'back_14',
    'product': 'back_15',
    'exhibition': 'back_16',
    'lottery': 'back_17',
    'educational': 'back_18',
    'art': 'back_19',
    'other': 'back_25',

    'outside_board_all_ads': 'back_23',
    'outside_board_new_ads': 'back_24',
    'on_board_all_ads': 'back_1',
    'on_board_new_ads': 'back_2',

    'all_vacancy': 'back_3',
    'new_vacancy': 'back_4',
    'all_bid': 'back_6',
    'new_bid': 'back_7',
    'all_call': 'back_9',
    'new_call': 'back_10', 
}


table_lst = ['posted_on_the_board', 'outside_board']


categories = [
    'missing',
    'assistance',
    'social',
    'product',
    'exhibition',
    'lottery',
    'educational',
    'art',
    'other'
]


main_category = [
    'all_vacancy',
    'new_vacancy',
    'all_bid',
    'new_bid',
    'all_call',
    'new_call' 
]