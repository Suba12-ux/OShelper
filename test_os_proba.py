from functools import lru_cache
from funk import *
import pathlib, os
from datetime import datetime, timedelta, date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, random

def CHupp(x):
    '''
    Функция для создания харакиристик.
    Получает список из одного Человека:
    Пример ----> ['Волков Матвей', 'Мужчина', 3]
    '''
    import random 
    import pathlib
    #txt1 = list(filter(lambda a: True if len([1 for i in a if str(i).isdigit()])!=0 else False ,txt))
    #txt2 = list(filter(lambda a: 3 in a or 2 in a, txt))
    general_c = ''
    if 3 in x or 2 in x:
        #general_features = []
        
        way1 = pathlib.Path(find_file('nch1.csv'))
        with way1.open('r', encoding='utf-8') as path:
            sl = list(map( lambda a: a[-1], list(csv.reader(path, delimiter=';'))))[1:]
            general_c += random.choice(sl)  + ' Так же надо заметить:'
        way2 = pathlib.Path(find_file('nch1.csv'))
        with way2.open('r', encoding='utf-8') as path:
            sl = list(map( lambda a: a[-1], list(csv.reader(path, delimiter=';'))))[1:]
            general_c += random.choice(sl)
        way3 = pathlib.Path(find_file('nch1.csv'))
        with way3.open('r', encoding='utf-8') as path:
            sl = list(map( lambda a: a[-1], list(csv.reader(path, delimiter=';'))))[1:]
            general_c += random.choice(sl) + '<----'
        if 'Мужчина' in x: general_c = f'Ученика был на {x[2]} уроках. За эти 3 дня: ---->' + general_c
        else: general_c = f'Ученика была на {x[2]} уроках. За эти 3 дня:' + general_c
    else: general_c += 'Н.Б'
    x.append(general_c)
    return x

def creating_templates(txt):
    txt1 = list(filter(lambda a: True if len([1 for i in a if str(i).isdigit()])!=0 else False ,txt))
    txt1 = list(map(lambda x: CHupp(x) , txt1))
    txt1 = list(map( lambda a: [*a[:-1], a[-1].replace('ученика', a[0].split()[-1])], txt1)) # ребенка, ученику
    txt1 = list(map( lambda a: [*a[:-1], a[-1].replace('ребенка', 'ученика')], txt1))
    txt1 = list(map( lambda a: [*a[:-1], a[-1].replace('ученику', a[0].split()[-1])], txt1))
    return txt1

txt = [['Волков Матвей', 'Мужчина', 3], ['Дамба Аян', 'Девушка', 0], ['Жарова Анастасия', 'Девушка', 2], ['Казенов Егор', 'Мужчина', 3], ['Климчук Владислав', 'Мужчина', 0], ['Коваленко Вячеслав', 'Мужчина', 3], ['Мишуков Егор', 'Мужчина', 1], ['Новиков Вадим', 'Мужчина', 3], ['Смирнов Егор', 'Мужчина', 3], ['Усманов Карим', 'Мужчина', 0], ['Халиуллин Айназ', 'Мужчина', 0], ['Шершнев Артем', 'Мужчина', 3], ['Эдилсултанова Айша', 'Девушка', 0], ['Бароненко Ярослав', 'Мужчина'], ['Головина Ярослава', 'Девушка'], ['Гуменюк Андрей', 'Мужчина'], ['Гумиров Даниил', 'Мужчина'], ['Дадажонова Даниэла', 'Девушка'], ['Лешукович Давуд', 'Мужчина'], ['Мамедова Афият', 'Девушка'], ['Разводовская Кира', 'Девушка'], ['Турищева Арина', 'Девушка']]
print(creating_templates(txt))
#print(CHupp(['Волков Максим', 'Мужчина', 3]))