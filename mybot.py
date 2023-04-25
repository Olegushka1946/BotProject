import telebot
import json
import requests
from config import keys
from BotException import ConvetionException, FinConvertion

bot = telebot.TeleBot("6202574943:AAHXeLnA_1PzrwBDsIOiw_8de38U__t_N9Y")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Хэй, хочешь узнать актуальный курс валют?\n\
	Введи команду /values чтобы узнать.")



@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
	TEXT = 'Какую валюту ты хочешь купить?\n\
	Доллары, Евро или Рубли?\n\
	Введи в следующем формате: "доллар рубль 15"\n\
	Где первое - валюта, которую хочешь купить,\n\
	второе валюта, на которую покупаешь\n\
	третье - количество покупаемой валюты'
	bot.reply_to(message,TEXT)



@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values)>3:
            raise ConvetionException('Много параметров')
        if len(values)<3:
            raise ConvetionException('Мало параметров')
        quete, base, amount = values
        quete_ticker, base_ticker = keys[quete], keys[base]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quete_ticker}&amount={amount}"
        payload = {}
        headers= {
            "apikey": "TaXjqHfrctaB1NBwQKqM4oSKM8UlIHEr"
        }
        response = requests.request("GET", url, headers=headers, data = payload)
        response = json.loads(response.content)
    except ConvetionException as e:
         bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
         bot.reply_to(message, f'Не удалось обработать запрос.\n {e}')
    else:
        text = f"За {amount} {quete} придется заплатить {round((response['result']), 2)} {base}"
        bot.send_message(message.chat.id, text)


bot.infinity_polling()
