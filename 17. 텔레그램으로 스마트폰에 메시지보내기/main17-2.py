import telegram

token = "5617984523:AAHdjz7dm232VP-tpaV2tzM1Nwk14ASBiYk"
id = "5406609735"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")