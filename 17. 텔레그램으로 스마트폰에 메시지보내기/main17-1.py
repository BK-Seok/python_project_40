import telegram

token = '5617984523:AAHdjz7dm232VP-tpaV2tzM1Nwk14ASBiYk'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)