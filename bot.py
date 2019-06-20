import telebot

bot = telebot.TeleBot('ваш токен')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Python', 'Циклы', 'Переменные', 'Кто создатель?')

print("Бот начал свою работу! Telegram чат: @aryntest_bot или t.me/aryntest_bot")
print("Что бы приостановить работу нажмите на клавиатуре [CTRL] + [C]")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start, для дальнейшего использования используй кнопки снизу!', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой друг!')
    elif message.text.lower() == 'здравствуй':
        bot.send_message(message.chat.id, 'Здравствуй, мой друг!')
    elif message.text.lower() == 'здравствуйте':
        bot.send_message(message.chat.id, 'Здравствуй, мой друг!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорой переписки!')
    elif message.text.lower() == 'кто создатель?':
        bot.send_message(message.chat.id, 'Создатель - Арын, 12-летний начинающий программист)). Его соц. сети: VK - https://vk.cc/9vScjc , Instagram - https://vk.cc/9vScHc , FB - https://vk.cc/9vScZJ , WhatsApp - https://vk.cc/9w2AnA')
    elif message.text.lower() == 'переменные':
        bot.send_message(message.chat.id, 'Переменная — это простейшая именованная структура данных, в которой может быть сохранён промежуточный или конечный результат работы программы. Переменную в Python создать очень просто — нужно присвоить некоторому идентификатору значение при помощи оператора присваивания «=». Никакого специального объявления переменных не требуется, первое присваивание переменной значения и является ее объявлением. Идентификатор в Python является "ссылкой" на хранимые в памяти данные. Источник: foxford.ru')
    elif message.text.lower() == 'python':
        bot.send_message(message.chat.id, 'Python — высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен. В то же время стандартная библиотека включает большой объём полезных функций. Python поддерживает структурное, объектно-ориентированное, функциональное, императивное и аспектно-ориентированное программирование. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений, высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты.')
    elif message.text.lower() == 'циклы':
        bot.send_message(message.chat.id, 'Цикл while - один из самых универсальных циклов в Python, поэтому довольно медленный. Выполняет тело цикла до тех пор, пока условие цикла истинно. Цикл for уже чуточку сложнее, чуть менее универсальный, но выполняется гораздо быстрее цикла while. Этот цикл проходится по любому итерируемому объекту (например строке или списку), и во время каждого прохода выполняет тело цикла. Источник: https://pythonworld.ru/')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат

    elif message.text.lower() == 'сук':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'сука':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'сучка':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'блять':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'блть':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'бля':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'збс':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'заебись':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'соси':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'сосни':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'хуй':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'ебать':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'ебат':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'ебало':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'пидор':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'пидр':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'ахуенно':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'ауенно':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'секс':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'секас':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'кака':
        bot.send_message(message.chat.id, 'Так не выражайся (>_<)')
    elif message.text.lower() == 'какашка':
        bot.send_message(message.chat.id, 'Так не выражайся (>_<)')
    elif message.text.lower() == 'пенис':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')
    elif message.text.lower() == 'писюн':
        bot.send_message(message.chat.id, 'Не матерись (>_<)')

#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат
#Не смтореть! Антимат

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()

print("Бот приостановил свою работу!")
print("Что бы выйти используй [ENTER]")

input()
