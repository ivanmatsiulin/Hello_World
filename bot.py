import telebot
from telebot import types

bot = telebot.TeleBot('2106447395:AAHvy9uUISutb4yvDE-Jrmr6WElfatYRgx8')     # наша переменная с токеном.
name = ''
surname = ''
age = 0


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! \nНапиши /reg для регистрации ")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDaLVhqmUqFg6Cp7wk2Zvg0JSd21IzbAACKgMAAs-71A4f8rUYf2WfMCIE")
    bot.send_message(message.chat.id, "")


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):  # получаем Имя
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):   # Получаем Фамилию
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):   # Получаем Возраст
    global age
    try:
        age = int(message.text)  # проверяем, что возраст введен корректно
    except ValueError:
        bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    else:
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
        keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + " " + surname + '?',
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)     # Обработка результата регистрации
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        # .... #код сохранения данных, или их обработки

        bot.send_message(call.message.chat.id, 'Запомню \U0001F604')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Напиши /reg')


bot.polling(none_stop=True, interval=0)
