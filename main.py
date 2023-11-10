import telebot
from telebot import types

bot = telebot.TeleBot('6703293760:AAHx21Oz8uc_2e_oGm2K6PWtJU-lcWUaUWw')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('CSS')
        btn2 = types.KeyboardButton('HTML')
        btn3 = types.KeyboardButton('JavaScript')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup)


    elif message.text == 'CSS':
        bot.send_message(message.from_user.id, '[ссылке](https://developer.mozilla.org/en-US/docs/Web/CSS)', parse_mode='Markdown')

    elif message.text == 'HTML':
        bot.send_message(message.from_user.id, '[ссылке](https://developer.mozilla.org/en-US/docs/Web/HTML)', parse_mode='Markdown')

    elif message.text == 'JavaScript':
        bot.send_message(message.from_user.id, '[ссылке](https://developer.mozilla.org/en-US/docs/Web/JavaScript)', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)