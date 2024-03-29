from os import environ

STATIC_URL = '/static/'

SESSION_CONFIGS = [
    dict(
        name='crowdinout',
        display_name='A public goods experiment',
        num_demo_participants=5,
        app_sequence=['crowdinout'],
    ),

    dict(
        name='crowdinout_highfine',
        display_name='A public goods experiment with high fine',
        num_demo_participants=5,
        app_sequence=['crowdinout_highfine'],
    ),

    dict(
        name='crowdinout_lowfine',
        display_name='A public goods experiment with low fine',
        num_demo_participants=5,
        app_sequence=['crowdinout_lowfine'],
    ),

    dict(
        name='crowdinout_pressure',
        display_name='A public goods experiment with peer pressure',
        num_demo_participants=5,
        app_sequence=['crowdinout_pressure'],
    ),
    dict(
        name='crowdinout_social_influence',
        display_name='A public goods experiment testing social influence',
        num_demo_participants=5,
        app_sequence=['crowdinout_social_influence'],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.035, participation_fee=10.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True
POINTS_CUSTOM_NAME = '分'


ADMIN_USERNAME = 'admin'

ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

#environ['OTREE_PRODUCTION'] = '1'

# don't share this with anybody.
SECRET_KEY = '-04aty%acnfw&pa*c7f2-hb+2fv57zcy4(pajjfs-t@n4jeqin'

INSTALLED_APPS = ['otree']

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
