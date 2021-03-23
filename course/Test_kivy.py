import os
import sys
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import webbrowser
import time

engine = pyttsx3.init()

cmd = {'chek_search': ('найти в интернете', 'нийди', 'найти', "поищи"),
       'chek_open': ("открой", "открыть")}


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
    RC = {'cmd': '', 'percent': 50}
    # извлечение адреса команд с и самих команд v
    for c, v in cmd.items():
        for x in v:
            vrt = fuzz.ratio(processed_voice, x)  # сравнение с имеющимися командами и тем что сказал пользователь
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC


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
        else:
            a = recognize_cmd(buffer)

            buffer = ''


def openn(text):
    if text == 'youtube':
        webbrowser.open('https://www.youtube.com/')
    elif text == "Яндекс":
        webbrowser.open('https://yandex.ru/')
    elif text == 'google':
        webbrowser.open('https://www.google.ru/')


def search(retur):
    webbrowser.open('https://yandex.ru/search/?lr=28&text={}'.format(retur))


while True:
    chek(say())

