import os
import sys
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import time
from tkinter import *

# engine = pyttsx3.init()

cmd1 = {'chek_search': ('найди', 'найти', "поищи"),
       'chek_translate': ("перевести", "переведи"),
       'name': ('кеша', 'алиса'),
       'question': ('как', 'где', 'почему', 'что'),
       'search':
           {'yandex': ('найди в яндексе', 'найти в яндексе', 'поищи в яндексе',
                       'найди в интернете', 'найти в интернете', 'поищи в интернете'),
            'google': ('найди в гугле', 'найти в гугле', 'поищи в гугле'),
            'youtube': ('найди в ютубе', 'найти в ютубе', 'поищи в ютубе',
                        'найди в youtube', 'найти в youtube', 'поищи в youtube'),
            'russia':('переведи с английского на руский', 'перевести английского на руский',
                      'перевод с английского на руский'),
            'english':('переводи с русского на английский', 'перевести с русского на английский',
                       ),
            }
       }

cmd = {
    # слова для выхода
    'exit': ('пока', 'выключить', 'досвидание', 'прощай'),
    # слова имени бота
    "name": ('алиса', 'ася', 'лиса', 'кеша', 'миша', 'kesha'),
    # слова помехи
    "trb_v1": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', "расскрыть", 'в', 'на', 'до'),
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

# def speak(what):
#     engine.say(what)
#     engine.runAndWait()
#     engine.stop()


def name(voice_text):
    text = voice_text.split()
    if text[0] in cmd1['name']:
        del text[0]
        chek(voice_text)
    else:
        chek(voice_text)


def say():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        w_y_s = r.recognize_google(audio, language="ru-RU").lower()
        print(w_y_s)
        return w_y_s
    except sr.UnknownValueError:
        print('голон не сраспознан')
        retur = say()
    return retur


def recognize_cmd(processed_voice):
    # в cmd будет присваивать адрес команды, percent уровень сравнение комнада должна совпадать на 75 %
    RC = {'cmd': '', 'percent': 75}
    # извлечение адреса команд с и самих команд v
    for c, v in cmd1['search'].items():
        for x in v:
            # сравнение с имеющимися командами и тем что сказал пользователь
            vrt = fuzz.ratio(processed_voice['command'], x)
            if vrt > RC['percent']:
                processed_voice['command'] = c
    return processed_voice


# функция получает текст из функции say и проверяет что нужно сделать найти, перевести...
def chek(voice_text):
    # Разделяет тест на слова и предлоги, после чего образует из них список
    text_voice = voice_text.split()
    # Опридиляет нужноли пользователю что-то найти
    if text_voice[0] in cmd1['chek_search']:
        len1 = 3
        buffer = separator(text_voice, len1)
        cmd_end_textcom = recognize_cmd(buffer)
        commands(cmd_end_textcom)
    # Опридиляет нужноли пользователю что-то перевести с en-ru или ru-en
    elif text_voice[0] in cmd1['chek_translate']:
        len1 = 5
        buffer = separator(text_voice, len1)
        cmd_end_textcom = recognize_cmd(buffer)
        commands(cmd_end_textcom)
    # ищет задаваемы вопрос без обращшение
    elif text_voice[0] in cmd1['question']:
        buffer = {'command': '', 'text_command': ''}
        for i in text_voice:
            buffer['text_command'] = buffer['text_command'] + i + ' '
        buffer['command'] = 'question'
        commands(buffer)
    # выход из системы
    elif text_voice[0] in ['пока', 'прощай', 'выход']:
        sys.exit()
    else:
        command(voice_text)


# резделяет команду и тест команды в раздельные списки словаря
def separator(text, len):
    buffer = {'command': '', 'text_command': ''}
    # text = text.split()
    for i in text:
        if len > 0:
            buffer['command'] = buffer['command'] + i + ' '
            len -= 1
        else:
            buffer['text_command'] = buffer['text_command'] + i + ' '
    return buffer


def command(voice):
    if voice.startswith(cmd["name"]):
        # удоляет имя бота в запросе
        for x in cmd["name"]:
            voice = voice.replace(x, '').strip()
        # удоляет слова помехи
        for x in cmd["trb_v1"]:
            voice = voice.replace(x, '').strip()

        # нечеткое сравнение со словами командами
        voice = recognize_cmd1(voice)
        # выполнение команд
        execute_cmd(voice)

    elif voice.startswith(cmd['exit']):
        # speak('Досвидание пользователь')
        sys.exit()
    # это необходимо если бот не услышал своё имя но команду нужно выполнить
    else:
        # удаляет имя бота в запросе
        for x in cmd["name"]:
            voice = voice.replace(x, '').strip()
        # удоляет слова помехи
        for x in cmd["trb_v1"]:
            voice = voice.replace(x, '').strip()

        # нечеткое сравнение со словами командами
        processed_voice = recognize_cmd1(voice)
        # выполнение команд
        execute_cmd(processed_voice)


# узнает что за команда была задана
def recognize_cmd1(processed_voice):
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


def execute_cmd(execution_command):
    # сказать текущее время
    if execution_command['cmd'] == 'time':
        print(execution_command['cmd'])
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    # откроет новую фкладку баузера yandex
    elif execution_command['cmd'] == 'web':
        print(execution_command['cmd'])
        webbrowser.open("https://yandex.ru/")
    # открывает youtube
    elif execution_command['cmd'] == 'youtube':
        print(execution_command['cmd'])
        webbrowser.open("https://www.youtube.com/")
    # открывает google
    elif execution_command['cmd'] == 'google':
        print(execution_command['cmd'])
        webbrowser.open("https://www.google.ru/")
    # открывает yandex
    elif execution_command['cmd'] == 'yandex':
        print(execution_command['cmd'])
        webbrowser.open("https://yandex.ru/")
    # открывает происковик и вводит в поисковик слова пользователя
    elif execution_command['cmd'] == 'search':
        print(execution_command['cmd'])
        search(say2())
    # открывает поисковик и переводит слова пользователя с русского на английский
    elif execution_command['cmd'] == 'translation_ru':
        print(execution_command['cmd'])
        translate_ru_en(say2())
    # открывает поисковик и переводит слова пользователя с английского на русский
    elif execution_command['cmd'] == 'translation_en':
        print(execution_command['cmd'])
        translate_en_ru(say2())
    # открывает радио
    elif execution_command['cmd'] == 'radio':
        print(execution_command['cmd'])
        webbrowser.open("https://europaplus.ru/?go=chart40%20")
    elif execution_command['cmd'] == 'taimer':
        print(execution_command['cmd'])
        timer(int(say2()))
    elif execution_command['cmd'] == 'zodiac':
        print(execution_command['cmd'])
        zodiac(say2())

# поридиляет команду и выполняет ее
def commands(text):
    if text['command'] == 'youtube':
        webbrowser.open('https://www.youtube.com/results?search_query={}'.format(text['text_command']))
    elif text['command'] == "yandex" or text['command'] == 'question':
        webbrowser.open('https://yandex.ru/search/?lr=28&text={}'.format(text['text_command']))
    elif text['command'] == 'google':
        webbrowser.open('https://www.google.ru/search?q={}'.format(text['text_command']))
    elif text['command'] == '':
        webbrowser.open('https://www.google.ru/search?q={}'.format(text['text_command']))


# name('найди как открыть банан')
# def assistent():
#     info['text'] = 'Я вас лашую'
#     cmdd()
#
# def cmdd():
#     while True:
#         name(say())

while True:
    name(say())

window = Tk()
# главное окно
window.resizable(width=False, height=False)
window.geometry('200x150')
window.title('Window')
window['bg'] = '#6c18f2'
info = Label(window, font=('Times New Roman', 15), text = '')
info.pack()
btn1 = Button(window, text = 'кнопка', command = assistent)
btn1.pack()


# функции акна
# def exit():
#     sys.exit()
#
#
#
# def setings():
#     win_fram.grid_forget()
#     win.grid_forget()
#     window.geometry('200x200')
#
# win = Label(window, width=45, heigh=7, bg='#f7cdf0',
#             font=('Times New Roman', 15),
#             anchor='nw',
#             text='привет как ваши дела что вы делаете')
# win.grid(row=0)
# win_fram = Frame(window, bg='#6c18f2')
# win_fram.grid(row=3, padx=10)
# # кнопки
# start = Button(win_fram, text='start', command=assistent)
# setings = Button(win_fram, text='setings', command = setings)
# command = Button(win_fram, text='command')
# exit = Button(win_fram, text='exit', command=exit)
# # упаковка кнопок
# start.grid(row=0, column=0, pady=10)
# setings.grid(row=0, column=1, pady=10)
# command.grid(row=0, column=2, pady=10)
# exit.grid(row=1, column=0, columnspan=3, stick='we')
window.mainloop()
