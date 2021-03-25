import os
import sys
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import time

engine = pyttsx3.init()

cmd = {'chek_search': ('найди', 'найти', "поищи"),
       'chek_translate': ("перевести", "переведи"),
       'search':
           {'yandex': ('найди в яндексе', 'найти в яндексе', 'поищи в яндексе',
                       'найди в интернете', 'найти в интернете', 'поищи в интернете'),
            'google': ('найди в гугле', 'найти в гугле', 'поищи в гугле'),
            'youtube': ('найди в ютубе', 'найти в ютубе', 'поищи в ютубе',
                        'найди в youtube', 'найти в youtube', 'поищи в youtube')
            }
       }


def speak(what):
    engine.say(what)
    engine.runAndWait()
    engine.stop()


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
    # в cmd будет присваивать адрес команды, percent уровень сравнение комнада должна совпадать на 50 %
    RC = {'cmd': '', 'percent': 75}
    # извлечение адреса команд с и самих команд v
    for c, v in cmd['search'].items():
        for x in v:
            # сравнение с имеющимися командами и тем что сказал пользователь
            vrt = fuzz.ratio(processed_voice['command'], x)
            if vrt > RC['percent']:
                processed_voice['command'] = c
    return processed_voice


def chek1(text):
    # счетчик что бы понять где заканчивается нужное действие например "найди"
    # после того как он нашел его счетски покажет где оно закончилось с учетом пробела после него
    chek_nummber = 0
    # хранилише что бы хранить части предложения для сравния поиска
    buffer_words = ''
    for i in text:
        chek_nummber += 1
        if i != ' ':
            buffer_words += i
        elif buffer_words in cmd['chek_translate']:
            len1 = 5
            buffer = chek2(text, len1)
            com_end_tcom = recognize_cmd(buffer)
            openn(com_end_tcom)
        elif buffer_words in cmd['chek_search']:
            len1 = 3
            buffer = chek2(text, len1)
            com_end_tcom = recognize_cmd(buffer)
            openn(com_end_tcom)


def chek2(text, len):
    buffer = {'command': '', 'text_command': ''}
    text = text.split()
    for i in text:
        if len > 0:
            buffer['command'] = buffer['command'] + i + ' '
            len -= 1
        else:
            buffer['text_command'] = buffer['text_command'] + i + ' '
    return buffer


def openn(text):
    if text['command'] == 'youtube':
        webbrowser.open('https://www.youtube.com/results?search_query={}'.format(text['text_command']))
    elif text['command'] == "yandex":
        webbrowser.open('https://yandex.ru/search/?lr=28&text={}'.format(text['text_command']))
    elif text['command'] == 'google':
        webbrowser.open('https://www.google.ru/search?q={}'.format(text['text_command']))


# chek1('найди в ютубе как открыть банан')
while True:
    chek1(say())
