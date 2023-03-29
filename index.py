from main import InstagramBot

list_users_tag = [
    '@user1',
    '@user2',
    '@user3',
    '@user4',
    '@user5',
    '@user6',
    '@user7',
    '@user8',
    '@user9'
]

bot = InstagramBot(
    'user',
    'pass',
    'CYRalzburR0',
    [50, 60, 70],
    3,
    200,
    list_users_tag,
    False
)

bot.login()
