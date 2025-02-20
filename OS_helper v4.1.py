from functools import lru_cache
import pathlib 
import os
from datetime import datetime, timedelta, date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def zapros_url(url, login, password):
    ''' 
    url - урл адресс группы
    login - логин от профиля
    password - пароль от профиля
    '''
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import time

    # Создаем экземпляр веб-драйвера
    driver = webdriver.Chrome()

    # Открываем страницу входа
    #url = 'https://lms.algoritmika.org/group/view/98668792'
    driver.get(url)

    # Вводим логин и пароль
 

    # Находим поля ввода логина
    login_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    # Заполняем поля ввода логина
    login_field.send_keys(login)

    # Нажимаем кнопку входа
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Находим поля ввода пароля
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    # Заполняем поля ввода
    password_field.send_keys(password)

    # Нажимаем кнопку входа
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # переходим к группам

    # Find all link elements within the div element
    links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='GroupStudent__body']//a[starts-with(@href, '/student/update/')]"))
    )

    data_group = []
    # Print the text of each link element
    for link in links: data_group.append(link.text)

    #****************************************************************************
    passed_box_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='GroupStudent__body']//div[@class='Expandable GroupStudent__item']//div[@class='Expandable__header']//div[@class='GroupStudent__row']//div[@class='GroupStudent__col GroupStudent__col__progress']//div[@class='StudentProgress']//div[@class='PassedBox__group']"))
    )
    txt = []
    # Iterate over each passed box element
    for passed_box_element in passed_box_elements:
        # Find all elements with class "PassedBox_box PassedBox_present glyphicon" within the passed box element
        present_elements = passed_box_element.find_elements(By.XPATH, ".//span[@class='PassedBox_box PassedBox_present glyphicon']")
        txt.append(len(present_elements))

    # Закрываем веб-драйвер
    time.sleep(3)
    driver.quit()

    txt = map(lambda a: [a], txt)
    return dict(zip(data_group, txt))

# Получаем текущую дату
today = date.today()

# Вычисляем дату три дня назад
three_days_ago = today - timedelta(days=3)

def vvod1():
    print('Введите группы согласно формату ввода.\n Для отправки введите [stop]')
    txt = []
    sl = ''
    while sl != 'stop':
        sl = input()
        if sl.isspace() or sl == '': continue
        else: txt.append(sl)
    txt2 = []
    for i in txt:
        if i.split()[-1].isalpha() and i != 'stop': txt2.append(i)
        else: continue
    print('Введите код посещения!')
    sx = input()
    gr = {txt2[k]: [sx[k]] for k in range(len(txt2))}
    return gr

def vvod2():
    print('Введите группы согласно формату ввода.\n Для отправки введите [stop]')
    txt = []
    sl = ''
    while True:
        sl =  input().lower()
        if sl == 'stop': break
        else: txt.append(sl.split()[:2])
    txt1 = []
    for i in range(len(txt)):
        sl = ''
        sl += txt[i][0]+' '+txt[i][-1]
        txt1.append(sl)
    return txt1

#@lru_cache #(maxsize=100)
def basedata():
    import os
    import pathlib
    dichen = {} #os.path.exists()
    way = pathlib.Path('genderData.txt').resolve()
    while True:
        if os.path.exists(way): 
            with way.open('r+', encoding='utf-8') as sk:
                exes =  sk.readlines()
                for i in exes:
                    s = convert_csv(i)
                    line1 = s.split('\t')
                    for j in line1:
                        line2 = j.split(': ')
                        dichen.setdefault(line2[0], line2[-1].split())
            return dichen
        else: 
            with way.open('w', encoding='utf-8') as sk:
                print('файл создан!')

def gender(txt, basedata):
    # txt = dict(), basedata = dict()
    if len(basedata) > 0: bs = [k for k in basedata]
    else: bs = []
    end_surname = 'а'
    end_name = ['а', 'я']
    for k in txt:
        if k in bs: txt[k].append(basedata[k][-1])
        else: 
            c = k.split()
            if c[0][-1] in end_surname and c[-1][-1] in end_name: txt[k].append('Девушка')
            elif not(c[0][-1] in end_surname):
                if c[-1][-1] in end_name: txt[k].append('Девушка')
                else: txt[k].append('Мужчина')
            elif c[0][-1] in end_surname:
                if not(c[-1][-1] in end_name): txt[k].append('Девушка')
                else: txt[k].append('Мужчина')
            else: txt[k].append('Мужчина')
    return txt

def ru_en_translate(txt):
    lang = {"А":'A', "Б":'B', "В":'V', "Г":'G', "Д":'D', "Е":'E', "Ж":'ZH', "З":'Z', "И":'I', "Й":'J', "К":'K', "Л":'L', "М":'M', "Н":'N', "О":'O', "П":'P', "Р":'R', "С":'S', "Т":'T', "У":'U', "Ф":'F', "Х":'H', "Ц":'TS', "Ч":'CH', "Ш":'SH', "Щ":'SHCH', "Ъ":'', "Ы":'Y', "Ь":'', "Э":'E', "Ю":'YA', "Я":'YA', ' ':' '}
    sl = ''
    for i in txt.upper():
        if i in lang: sl += lang[i]
        else: continue 
    return sl.lower().title()

def convert_csv(txt):
        # txt = dict()
        txt = str(txt)
        txt = txt.replace('{', '')
        txt = txt.replace('}', '')
        txt = txt.replace("'", '')
        txt = txt.replace('"', '')
        txt = txt.replace(',', '')
        txt = txt.replace(']', '\t')
        txt = txt.replace('[', '')
        txt = txt.replace('\n', '')
        return txt

def grup(txt):
    x1 = [k for k in txt]
    #x2 = input('Введи код посещения:') # 0121301300210 **********************************************************
    for k in range(len(x1)):
        txt[x1[k]].append(x2[k])
    return txt

def chupp(txt): 
    import random 
    import pathlib


    with pathlib.Path('./upchar/upchar4.0.txt').resolve().open('r', encoding='utf-8') as lib1:
        file1 = lib1.read()
        file1 = file1.replace('\n', '')
        file1 = file1.split('.')
    with pathlib.Path('./upchar/upchar2.0.txt').resolve().open('r', encoding='utf-8') as lib2:
        file2 = lib2.read()
        file2 = file2.replace('\n', '')
        file2 = file2.split('.')
    with pathlib.Path('./upchar/upchar3.0.txt').resolve().open('r', encoding='utf-8') as lib3:
        file3 = lib3.read()
        file3 = file3.replace('\n', '')
        file3 = file3.split('.')
    with pathlib.Path('./upchar/dbup.txt').resolve().open('r', encoding='utf-8') as way2:
        file4 = way2.readlines()
    tx = [k for k in txt]
    c = 0
    #[txt[i].append('') for i in txt]
    for i in txt:
        txt[i].append('')
        if '2' in txt[i] or '3' in txt[i] or 2 in txt[i] or 3 in txt[i]:
            txt[i][-1] += f'\tученики был на {txt[i][0]} уроках. '.lower()
            txt[i][-1] += file1[random.randint(0, len(file1)-1)].lower()+'. '
            txt[i][-1] += file4[random.randint(0, len(file4)-1)].lower()
            txt[i][-1] += 'Так же хочу пожелать на будущее: '.lower()
            txt[i][-1] += file3[random.randint(0, len(file3)-1)].lower()+'. '
            
        elif not('2' in txt[i] or '3' in txt[i] or 2 in txt[i] or 3 in txt[i]): txt[i][-1] += '\tН.Б'
    return txt

def remake(txt):
    for k in txt:
        if 'Девушка' in txt[k]:
            txt[k][-1] = txt[k][-1].replace('ученики', k.split()[-1])
            txt[k][-1] = txt[k][-1].replace('\n', '')
            txt[k][-1] = txt[k][-1].replace('ваня', k.split()[-1])
            txt[k][-1] = txt[k][-1].replace('ученика', '')
            txt[k][-1] = txt[k][-1].replace('ученику', 'ей')
            txt[k][-1] = txt[k][-1].replace('ученик', k.split()[-1])
            txt[k][-1] = txt[k][-1].replace('он', 'она')
            txt[k][-1] = txt[k][-1].replace('его', 'ее')
            txt[k][-1] = txt[k][-1].replace('этот', '')
            txt[k][-1] = txt[k][-1].replace('лся', 'лась')
            txt[k][-1] = txt[k][-1].replace('ым', 'ой')
            txt[k][-1] = txt[k][-1].replace('был', 'была')
            txt[k][-1] = txt[k][-1].replace('ен', 'ена')
            for j in txt[k][-1].split():
                if j[-1] == 'л':
                    c = txt[k][-1].find(j)
                    #ts = txt[k][-1][c:len(j)+1]+'а'
                    txt[k][-1] = txt[k][-1].replace(j, j+'а')

        elif 'Мужчина' in txt[k]:
            txt[k][-1] = txt[k][-1].replace('\n', '')
            txt[k][-1] = txt[k][-1].replace('ученики', k.split()[-1])
            txt[k][-1] = txt[k][-1].replace('ваня', k.split()[-1])
            txt[k][-1] = txt[k][-1].replace('этот', '')
            txt[k][-1] = txt[k][-1].replace('ученика', '')
            txt[k][-1] = txt[k][-1].replace('ученику', 'ему')
    return txt

#************************************** ОСНОВНОЙ ЦИКЛ КОДА **************************************

#************************************** ЭТАП 1 **************************************
print('Начнем ?')
while void_loop := input().lower() != 'хватит':
    url = input('Веди url адрес группы:\n')
    login = input('Введи логин от профиля!\n')
    password = input('Введи пароль от профиля!\n')
    
    txt1 = zapros_url(url, login, password)

    txt = gender(txt1, basedata())

    #************************************** ЭТАП 2 **************************************

    with pathlib.Path(r'genderData.txt').resolve().open('a', encoding='utf-8') as lende:
        print(txt, file=lende)
        print(txt)
        print('Этап 3')

    #************************************** ЭТАП 3 **************************************
    way = pathlib.Path(r'os_group.txt').resolve()
    with way.open('a', encoding='utf-8') as lib:
        ts = remake(chupp(txt))
        print("Группа:", three_days_ago, file=lib)
        for k in ts:
            print(k, ts[k][2], file=lib)
        print('****************************************************************************', file=lib)
        print('Данные сохранены в текстовый файл os_group', f'Путь сохронения: {way}', sep='\n')
    print('Если хотите закончиь введите [хватит]')
    

