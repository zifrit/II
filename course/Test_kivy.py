import os
import sys
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import time
from tkinter import *

engine = pyttsx3.init()

cmd = {'chek_search': ('найди', 'найти', "поищи"),
       'chek_translate': ("перевести", "переведи"),
       'name': ('кеша', 'алиса'),
       'question': ('как', 'где', 'почему', 'что'),
       'search':
           {'yandex': ('найди в яндексе', 'найти в яндексе', 'поищи в яндексе',
                       'найди в интернете', 'найти в интернете', 'поищи в интернете'),
            'google': ('найди в гугле', 'найти в гугле', 'поищи в гугле'),
            'youtube': ('найди в ютубе', 'найти в ютубе', 'поищи в ютубе',
                        'найди в youtube', 'найти в youtube', 'поищи в youtube'),
            }
       }


def speak(what):
    engine.say(what)
    engine.runAndWait()
    engine.stop()


def name(voice_text):
    text = voice_text.split()
    if text[0] in cmd['name']:
        del text[0]
        chek(text)
    else:
        chek(text)

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
    for c, v in cmd['search'].items():
        for x in v:
            # сравнение с имеющимися командами и тем что сказал пользователь
            vrt = fuzz.ratio(processed_voice['command'], x)
            if vrt > RC['percent']:
                processed_voice['command'] = c
    return processed_voice


# функция получает текст из функции say и проверяет что нужно сделать найти, перевести...
def chek(voice_text):
    # Разделяет тест на слова и предлоги, после чего образует из них список
    # text = voice_text.split()
    # Опридиляет нужноли пользователю что-то найти
    if voice_text[0] in cmd['chek_search']:
        len1 = 3
        buffer = separator(voice_text, len1)
        cmd_end_textcom = recognize_cmd(buffer)
        commands(cmd_end_textcom)
    # Опридиляет нужноли пользователю что-то перевести с en-ru или ru-en
    elif voice_text[0] in cmd['chek_translate']:
        len1 = 3
        buffer = separator(voice_text, len1)
        cmd_end_textcom = recognize_cmd(buffer)
        commands(cmd_end_textcom)
    elif voice_text[0] in cmd['question']:
        buffer = {'command': '', 'text_command': ''}
        for i in voice_text:
            buffer['text_command'] = buffer['text_command'] + i + ' '
        buffer['command'] = 'question'
        commands(buffer)
    elif voice_text[0] in ['пока', 'прощай']:
        sys.exit()


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


# поридиляет команду и выполняет ее
def commands(text):
    if text['command'] == 'youtube':
        webbrowser.open('https://www.youtube.com/results?search_query={}'.format(text['text_command']))
    elif text['command'] == "yandex" or text['command'] == 'question':
        webbrowser.open('https://yandex.ru/search/?lr=28&text={}'.format(text['text_command']))
    elif text['command'] == 'google':
        webbrowser.open('https://www.google.ru/search?q={}'.format(text['text_command']))
    elif text['command'] == ' ':
        webbrowser.open('https://www.google.ru/search?q={}'.format(text['text_command']))


# name('найди как открыть банан')
# while True:
#     name(say())

window = Tk()

window.resizable(width=True, height=True)
window.geometry('500x500')
window.title('Window')
window['bg'] = '#42424d'
window.mainloop()
