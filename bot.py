import telebot
from telebot import types
import sqlite3
from config import TOKEN

conn = sqlite3.connect('bot.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,surname TEXT,age INT,answer_1 TEXT,answer_2 TEXT,answer_3 TEXT,answer_4 TEXT,answer_5 TEXT,
    answer_6 TEXT,answer_7 TEXT,answer_8 TEXT,answer_9 TEXT,answer_10 TEXT) ''')

bot = telebot.TeleBot(TOKEN)  # наша переменная с токеном.

name = ''
surname = ''
age = 0
ans_1 = ''
ans_2 = ''
ans_3 = ''
ans_4 = ''
ans_5 = ''
ans_6 = ''
ans_7 = ''
ans_8 = ''
ans_9 = ''
ans_10 = ''


def db_table_val(name, surname, age, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10):
    # функция для записи данных пользователя
    cursor.execute('''INSERT INTO tab_1(name, surname, age, answer_1, answer_2, answer_3, answer_4, answer_5,
     answer_6, answer_7, answer_8, answer_9, answer_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (name, surname, age, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! \nНапиши /reg для регистрации\n или /help для вызова справки  ")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDaLVhqmUqFg6Cp7wk2Zvg0JSd21IzbAACKgMAAs-71A4f8rUYf2WfMCIE")


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Напиши /reg для регистрации ")


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
    elif message.text == '/start_questions':
        bot.send_message(message.from_user.id, "Насколько вероятно, что вы порекомендуете мероприятие "
                                               "другу или коллеге? (по 10-бальной шкале)")
        bot.register_next_step_handler(message, get_answers_on_questions)

    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):  # получаем Имя
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):  # Получаем Фамилию
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):  # Получаем Возраст
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


@bot.callback_query_handler(func=lambda call: True)  # Обработка результата регистрации
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, 'Запомню \U0001F604')
        bot.send_message(call.message.chat.id, 'Напиши /start_questions, чтобы начать опрос')
        # нужно улучшить переход на опрос
        # get_answers_on_questions()
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Напиши /reg')


def get_answers_on_questions(message):
    global ans_1
    ans_1 = message.text
    bot.send_message(message.from_user.id, 'В целом, как бы Вы оценили мероприятие?')
    bot.register_next_step_handler(message, question_2)


def question_2(message):
    global ans_2
    ans_2 = message.text
    bot.send_message(message.from_user.id, 'Что тебе понравилось на мероприятии?')
    bot.register_next_step_handler(message, question_3)


def question_3(message):
    global ans_3
    ans_3 = message.text
    bot.send_message(message.from_user.id, 'Что тебе НЕ понравилось на мероприятии?')
    bot.register_next_step_handler(message, question_4)


def question_4(message):
    global ans_4
    ans_4 = message.text
    bot.send_message(message.from_user.id, 'Как было организовано мероприятие?')
    bot.register_next_step_handler(message, question_5)


def question_5(message):
    global ans_5
    ans_5 = message.text
    bot.send_message(message.from_user.id, 'На сколько персонал был дружелюбен?')
    bot.register_next_step_handler(message, question_6)


def question_6(message):
    global ans_6
    ans_6 = message.text
    bot.send_message(message.from_user.id, 'Был ли персонал Вам полезен?')
    bot.register_next_step_handler(message, question_7)


def question_7(message):
    global ans_7
    ans_7 = message.text
    bot.send_message(message.from_user.id, 'Какой процент нужной информации вы получили на мероприятии?')
    bot.register_next_step_handler(message, question_8)


def question_8(message):
    global ans_8
    ans_8 = message.text
    bot.send_message(message.from_user.id, 'Мероприятие длилось долго или слишком быстро прошло?')
    bot.register_next_step_handler(message, question_9)


def question_9(message):
    global ans_9
    ans_9 = message.text
    bot.send_message(message.from_user.id, 'Напишите, что хотите о мероприятии')
    bot.register_next_step_handler(message, question_10)


def question_10(message):
    global ans_10
    ans_10 = message.text
    db_table_val(name, surname, age, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9, ans_10)
    bot.send_message(message.chat.id, 'Спасибо, что приняли участие в опросе!\nВсего наилучшего!')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDgMphu5oEwaxeNBpChQIH2C_Xp6Y_YAACJQMAAs-71A5-9qElD4i0vCME')


bot.polling(none_stop=True, interval=0)
