import os
import sys
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import time

engine = pyttsx3.init()

# команды бота
cmd = {
    # слова для выхода
    'exit': ('пока', 'выключить', 'досвидание', 'прощай'),
    # слова имени бота
    "name": ('алиса', 'ася', 'лиса', 'кеша', 'миша', 'kesha'),
    # слова помехи
    "trb_v1": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', "расскрыть", 'в', 'на', 'до'),
    'trb_v2': (''),
    'poisk': {'web': ('найди', 'найти', 'поищи', 'поиск'),
              'translate': ('переведи', 'перевести')},
    # команды бота
    "cmd": {
        'time': ("сколько вермя", "время", "часы", "который сейчас час", "который час", "сколько часов",),
        'radio': ('включи радео', 'радио'),
        'web': ("страница", 'станицу', 'баузер', 'browser', 'web browser', 'webbrowser', 'веббраузер', 'веб браузер'
                , 'сайт', 'открой страницу', 'открыть брайзер', 'интернет'),
        'youtube': ("ютуб", "youtube", 'you tube', 'открыть ютуб', 'открыть youtube', 'открыть you tube'),
        'google': ('google', 'открыть гугл', 'открыть google'),
        'yandex': ("yandex", 'яндекс', 'открыть яндекс', "открыть yandex"),
        'vk': ('vr', 'вк', 'вконтакте', 'в контакте', 'контакты'),
        'search': ('найди', 'найти', 'поиск', 'найти в интернете', 'найди в google'),
        'translation_ru': ('перевод с русского на английский', 'перевести с русского на английский',
                           'переведи слово с русского на английский', 'перевести на английски', 'перевод на английский'),
        'translation_en': ('перевод с английского на русский', 'перевести с английского на русский',
                           'переведи слово с английского на русский', 'перевести на русский', 'перевод на русский'),
        'taimer': ('таймер', 'timer'),
        'zodiac': ('какой знак зодиака у меня', 'знак зодиака', 'зодиак', 'задиак', 'знак задиак'),
    }
}


# позволяет боту говорить
def speak(what):
    engine.say(what)
    engine.runAndWait()
    engine.stop()


# функция которая слушает пользователя переводя аудио дорожку в тест, присваивая текст к глобально переменно
def say():

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        w_y_s = r.recognize_google(audio, language="ru-RU").lower()
        print('вы сказали: ', w_y_s)
        speak(w_y_s)
        return w_y_s
    except sr.UnknownValueError:
        print('голон не сраспознан')
        retur = say()
    return retur


# копия say только используется для ввода текста в поисковик
def say2():
    speak('что ?')
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        w_y_s = r.recognize_google(audio, language="ru-RU").lower()
        print('вы сказали: ', w_y_s)
        speak(w_y_s)
        return w_y_s
    except sr.UnknownValueError:
        print('голон не сраспознан')
        retur = say2()
    return retur


# функции которая получает из say перемену с текстом, удоляя из текста слова помехи оставляя конкретные команды
def command(voice):
    if voice.startswith(cmd["name"]):
        # удоляет имя бота в запросе
        for x in cmd["name"]:
            voice = voice.replace(x, '').strip()
        # удоляет слова помехи
        # for x in cmd["trb_v1"]:
        #     voice = voice.replace(x, '').strip()

        # нечеткое сравнение со словами командами
        voice = recognize_cmd(voice)
        # выполнение команд
        execute_cmd(voice)

    elif voice.startswith(cmd['exit']):
        speak('Досвидание пользователь')
        sys.exit()
    # это необходимо если бот не услышал своё имя но команду нужно выполнить
    else:
        # удаляет имя бота в запросе
        for x in cmd["name"]:
            voice = voice.replace(x, '').strip()
        # удоляет слова помехи
        # for x in cmd["trb_v1"]:
        #     voice = voice.replace(x, '').strip()


        a = chek(voice)
        # нечеткое сравнение со словами командами
        processed_voice = recognize_cmd(voice)
        # выполнение команд
        execute_cmd(processed_voice)


def chek(text):
    # счетчик что бы понять где заканчивается нужное действие например "найди"
    # после того как он нашел его счетски покажет где оно закончилось с учетом пробела после него
    chek_nummber = 0
    # хранилише что бы хранить части предложения для сравния поиска
    buffer = ''
    for i in text:
        chek_nummber += 1
        if i != ' ':
            buffer += i
        elif buffer in cmd['poisk']['web']:


            buffer = ''


# узнает что за команда была задана
def recognize_cmd(processed_voice):
    # в cmd будет присваивать адрес команды, percent уровень сравнение комнада должна совпадать на 50 %
    RC = {'cmd': '', 'percent': 50}
    # извлечение адреса команд с и самих команд v
    for c, v in cmd['cmd'].items():
        for x in v:
            vrt = fuzz.ratio(processed_voice, x)  # сравнение с имеющимися командами и тем что сказал пользователь
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC


def zodiac(date):
    date_numbers = int(date[0:2])
    date_month = date[3:]
    if (date_numbers >= 22 and date_month == 'декабря') or (date_numbers <= 20 and date_month == 'января'):
        print('козерог')
        speak('козерок')
    elif (date_numbers >= 21 and date_month == 'января') or (date_numbers <= 19 and date_month == 'февраля'):
        print('водолей')
        speak('водолей')
    elif (date_numbers >= 20 and date_month == 'февраля') or (date_numbers <= 20 and date_month == 'марта'):
        print('рыба')
        speak('рыба')
    elif (date_numbers >= 21 and date_month == 'марта') or (date_numbers <= 20 and date_month == 'апреля'):
        print('овен')
        speak('овен')
    elif (date_numbers >= 21 and date_month == 'апреля') or (date_numbers <= 21 and date_month == 'мая'):
        print('телец')
        speak('телец')
    elif (date_numbers >= 22 and date_month == 'мая') or (date_numbers <= 21 and date_month == 'июнь'):
        print('близнецы')
        speak('близнецы')
    elif (date_numbers >= 22 and date_month == 'июня') or (date_numbers <= 23 and date_month == 'июля'):
        print('рак')
        speak('рак')
    elif (date_numbers >= 24 and date_month == 'июля') or (date_numbers <= 23 and date_month == 'августа'):
        print('лев')
        speak('лев')
    elif (date_numbers >= 24 and date_month == 'августа') or (date_numbers <= 23 and date_month == 'сентября'):
        print('дева')
        speak('дева')
    elif (date_numbers >= 24 and date_month == 'сентября') or (date_numbers <= 23 and date_month == 'октября'):
        print('весы')
        speak('весы')
    elif (date_numbers >= 24 and date_month == 'октября') or (date_numbers <= 23 and date_month == 'ноября'):
        print('скорпион')
        speak('скорпион')
    elif (date_numbers >= 23 and date_month == 'ноября') or (date_numbers <= 21 and date_month == 'декабря'):
        print('телец')
        speak('телец')


def timer(minutes):
    while True:
        second = 0
        minute = 0
        hour = 0
        minutes = minutes * 60
        for _ in range(minutes):
            time.sleep(1)
            second += 1
            if second == 60:
                minute += 1
                second = 0
            if minute == 60:
                hour = 1
                minute = 0
        break
    print('hour:', hour, 'minute:', minute, 'second:', second)
    speak('время закончилось')


# из say2 поступает слова пользователя которые с помощью format вставляются в url адрес после с использованием
# библиотеки webbrowser открывается ссылка со вставленными словами пользователя
def search(retur):
    webbrowser.open('https://yandex.ru/search/?lr=28&text={}'.format(retur))


def translate_ru_en(retur):
    webbrowser.open('https://translate.yandex.ru/?utm_source=wizard&lang=ru-en&text={}'.format(retur))


def translate_en_ru(retur):
    webbrowser.open('https://translate.yandex.ru/?utm_source=wizard&lang=en-ru&text={}'.format(retur))


# функция выполнения команд
def execute_cmd(execution_command):
    # сказать текущее время
    if execution_command['cmd'] == 'time':
        print(execution_command['cmd'])
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    # откроет новую фкладку баузера yandex
    if execution_command['cmd'] == 'web':
        print(execution_command['cmd'])
        webbrowser.open("https://yandex.ru/")
    # открывает youtube
    if execution_command['cmd'] == 'youtube':
        print(execution_command['cmd'])
        webbrowser.open("https://www.youtube.com/")
    # открывает google
    if execution_command['cmd'] == 'google':
        print(execution_command['cmd'])
        webbrowser.open("https://www.google.ru/")
    # открывает yandex
    if execution_command['cmd'] == 'yandex':
        print(execution_command['cmd'])
        webbrowser.open("https://yandex.ru/")
    # открывает происковик и вводит в поисковик слова пользователя
    if execution_command['cmd'] == 'search':
        print(execution_command['cmd'])
        search(say2())
    # открывает поисковик и переводит слова пользователя с русского на английский
    if execution_command['cmd'] == 'translation_ru':
        print(execution_command['cmd'])
        translate_ru_en(say2())
    # открывает поисковик и переводит слова пользователя с английского на русский
    if execution_command['cmd'] == 'translation_en':
        print(execution_command['cmd'])
        translate_en_ru(say2())
    # открывает радио
    if execution_command['cmd'] == 'radio':
        print(execution_command['cmd'])
        webbrowser.open("https://europaplus.ru/?go=chart40%20")
    if execution_command['cmd'] == 'taimer':
        print(execution_command['cmd'])
        timer(int(say2()))
    if execution_command['cmd'] == 'zodiac':
        print(execution_command['cmd'])
        zodiac(say2())


speak('Здравствуйте пользователь')

while True:
    command(say())

