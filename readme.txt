Telegram-бот на Python

Введение
Часть 1: Регистрация бота
Часть 2: Установка библиотек
Часть 3: Получаем сообщения и говорим
Часть 4: Кнопки и ветки сообщений
Часть 5: Добавление стикеров и эмоджи
Часть 6: Подключение к SQLite
Часть 7: Перспективы развития

Введение
Приветствую всех, кого заинтересовала моя работа в рамках курса "Python-разработчик", и благодарю за внимание
Данный телеграм-бот был создан для того чтобы помочь организаторам различных мероприятий получить обратную связь от
их посетителей с помощью телеграма, что имеет свои плюсы.
- Моментальный ответ пользователю;
- Удобство в пользовании, общение по принципу «вопрос-ответ» и текстовые задания под силу давать даже совсем неопытному
пользователю мессенджера;
- Не требуют установки дополнительных программ, приложений и т.п. Все общение с ботом ведется напрямую через мессенджер;
- Безопасность личных данных – боты работают исключительно по заданным командам.

Часть 1
Для регистрации нужно найти бота @BotFather, написать ему /start, или /newbot,
 заполнить поля, которые он спросит (название бота и его короткое имя), и получить сообщение с токеном бота и ссылкой
 на документацию. Токен нужно надёжно сохранить, так как это единственный ключ для авторизации бота и
 взаимодействия с ним. В нашем случае, я создайл config.py, где он будет храниться под переменной TOKEN, и затем в
 основном файле bot.py импортируем эту переменную.
            from config import TOKEN
            bot = telebot.TeleBot(TOKEN)
Более подробную информацию можно прочитать на оф.сайте https://tlgrm.ru/docs/bots

Часть 2
Устанавливаем библиотеку PyTelegramBotAPI (Telebot) с помощью установщика pip
(https://pip.pypa.io/en/stable/installation/)
>>> pip install pytelegrambotapi (в терминале)

Часть 3
Импортируем библиотеку и прописываем Токен
            import telebot                                    <1>
            bot = telebot.TeleBot(TOKEN)                     <13>
Эта строка в коде бота отвечает за постоянную обработку информации, приходящей с серверов Telegram:
            bot.polling(none_stop=True, interval=0)          <181>
После этого нам нужно написать обработчики сообщений. Обработчики сообщений определяют
фильтры, которые должно пройти сообщение. Если сообщение проходит фильтр, вызывается декорированная функция,
и входящее сообщение передается в качестве аргумента.

Я использовал /start и /help команды:
            @bot.message_handler(commands=['start'])         <38>
            @bot.message_handler(commands=['help'])          <44>
и обработчик для получения текстовых сообщений:
            @bot.message_handler(content_types=['text'])     <50...>

Для отправки ботом сообщений используем метод
            bot.send_message(message.chat.id, '')            <40...>

Создадим функцию, которая бы обрабатывала вх. сообщения и направляла бы диалог в разные ветви:
- пройти регистрацию опрашиваемого
- начать опрос (эта команда видна после регистрации)
- если ввел что-то другое(исключение), то пройти регистрацию
            @bot.message_handler(content_types=['text'])     <50>
            def start(message):
                if message.text == '/reg':
                ...
                elif message.text == '/start_questions':
                ...
                else:
                ...
Далее, используя ф-ции get_name, get_surname, get_age получаем информацию об опрашиваемом (регистрируем)
А для перехода к следующей функции применяем метод register_next_step_handler:
            bot.register_next_step_handler(message, get_name)<54...>

Часть 4

В функции get_age:
- применили обработку исключений, позволяющую пользователю вводить возраст цифрами
- вставили клавиатуру InlineKeyboard (привязанную к сообщению, изпользующая обратный вызов (CallbackQuery),
вместо отправки сообщения с обыкновенной клавиатуры) для подтверждения информации о пользователе(корректна ли она?)
            keyboard = types.InlineKeyboardMarkup()             <89>
Чтобы вставить клавиатуру необходимо импортировать types из библиотеки telebot
            from telebot import types                           <2>
Но клавиатура не работает сама по себе, для неё нужен тоже обработчик
            @bot.callback_query_handler(func=lambda call: True) <98>

Далее пользователь пишет /start_questions и начинается опрос. Для каждого вопроса мы создали отдельную функцию,
ответ на который переопределит уникальную переменную для каждого вопроса

Часть 5

В Python встроен Юникод, поэтому можно без проблем вставлять эмоджи без дополнительных библиотек. Например
             bot.send_message(call.message.chat.id, 'Запомню \U0001F604') <101>
Мне было удобно выбирать с этого ресурса: unicode.org/emoji/charts/full-emoji-list.html

И конечно куда без стикеров! Они очень популярны и придают беседе эмоциональный контекст
Мы можем их применить используя метод sendStiker, а для того чтобы узнать кодовое имя стикера, нужно отправить желаемый
стикер боту "Get Sticker ID" в телеграме

    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDaLVhqmUqFg6Cp7wk2Zvg0JSd21IzbAACKgMAAs-71A4f8rUYf2WfMCIE")
    <41>
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDgMphu5oEwaxeNBpChQIH2C_Xp6Y_YAACJQMAAs-71A5-9qElD4i0vCME')
    <177>

Часть 6
Импортируем встроенный SQLite
              import sqlite3                                      <3>
Создадим БД.
Далее мы создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
              conn = sqlite3.connect('bot.db', check_same_thread=False)
              cursor = conn.cursor()                              <8>
Создадим таблицу, с 14 столбцами, где будут записываться наши переменные, которые соответствуют данным регистрации
пользователя и ответам на вопросы опросника
                cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,surname TEXT,age INT,answer_1 TEXT,answer_2 TEXT,answer_3 TEXT,answer_4 TEXT,answer_5 TEXT,
                    answer_6 TEXT,answer_7 TEXT,answer_8 TEXT,answer_9 TEXT,answer_10 TEXT) ''') <9>
Создадим функцию, которая будет записывать данные пользователя в нашу таблицу БД
                def db_table_val(name, surname, age, ans_1, ans_2, ans_3, ans_4, ans_5, ans_6, ans_7, ans_8, ans_9,
                ans_10):
                ...
                                                                  <30>
Обращаемся к ней после окончания опроса
                   db_table_val(name, surname ... ans_10)         <175>
С помощью SQLite Studio можно убедиться что все наши данные записываются в нашу таблицу


Часть 7: Перспективы развития
- Переписать вопросы, которые взяты с www.surveymonkey.ru/mp/post-event-survey-questions/ в моем вольном переводе
- Переделать на работу с вебхуками
- Деплоинг на сервер, например Heroku

Выводы
В результате я создал телеграм-бота, который может помочь получить обратную связь от посетителей мероприятия в удобной
и современной форме, и помочь организаторам сделать свои мероприятия еще лучше
