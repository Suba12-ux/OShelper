from functools import lru_cache
import pathlib, os
from datetime import datetime, timedelta, date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, csv

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

    # Получаем статус и название группы ******************************************

    gro = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='EditableArea__input']"))
    )
    x = list(filter(lambda a: a!='', [gs.text for gs in gro]))

    # Закрываем веб-драйвер
    driver.quit()

    txt = list(map(int, txt))
    
    return data_group, txt, x

def find_file(file_name):
    '''Получает имя файла в формате str'''
    # перебераем все диски:
    for drive in ['C:', 'A', 'D:', 'E:', 'B', 'F', 'G']: # нужно заменить при необходимости
        for root, dirs, files in os.walk(drive):
            if file_name in files: return os.path.join(root, file_name) #проверка на совпадения
    return None

def gender(txt, x):
    '''
    Функция на определение пола.
    Получает два позиционных аргумента. 
        1-Список людей: ['Фамилия Имя', 'Фамилия Имя', 'Фамилия Имя', 'Фамилия Имя', 'Фамилия Имя']
        2-Список кортежей из имен людей с полом:
            [
             (name surname : gender), 
             (name surname : gender), 
             (name surname : gender)
            ]
    '''
    way = pathlib.Path('GenderData.csv').resolve()
    col = ['N/S', 'gender']
    if not way.exists(): 
        with way.open('w', encoding='utf-8') as lib:
            writer = csv.writer(lib, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(col)

    with way.open('r', encoding='utf-8', newline='') as path_1:
        data_base = csv.reader(path_1, delimiter=';')
        #sv = list(map(lambda a: [a, pol(a)], txt))
        sv = txt
        test = list(data_base)
        for i in range(len(sv)):
            for j in test:
                if sv[i] in j: sv[i] = j
        for i in range(len(sv)):
            if type(sv[i]) == str: sv[i] = [sv[i], pol(sv[i])]
        

        with way.open('r+', encoding='utf-8', newline='') as path_2: 
            path_2.seek(0)
            writer = csv.writer(path_2, delimiter=';')
            data_base_w = csv.reader(path_2, delimiter=';')
            tester = list(data_base_w)
            if 0<= len(tester) <= 2: 
                for i in sv: writer.writerow(i)
            else:
                prod = list(map(lambda a: a[0], tester))
                for i in sv:
                    if  not i[0] in prod: writer.writerow(i)
    [sv[i].append(k) for i, k in enumerate(x)]
    return sv

def users():
    '''
    Аргументов не принимает, создет файл users.txt в корневой части папки проета.
    Проверка профелей так же идет из файла users.txt.
    '''
    UL_key = sum([ord(i) for i in input('Введите свой уникальный ключ шифрования.\nИли придумайте и не забывайте =>.\nЭто может быть все что угодно даже слова или придложения.\n')])  
    lib_puth = pathlib.Path('users.csv').resolve()

    # создаем файл, если он не существует
    if not os.path.exists(lib_puth):
        with open(lib_puth, 'w') as path_:
            writer = csv.writer(path_, delimiter=';') # просто создаем пустой файл csv c элементами 'login','pass','ULk'
            writer.writerow(['login','pass','ULk'])

    with lib_puth.open('r+', encoding='utf-8') as prof:

        sl = csv.DictReader(prof, delimiter=';', quotechar='"')
        exod = SES(str(UL_key), UL_key)
        for i in sl:
            if exod == i['ULk']:  # если профиль найден
                return decod(i['login'], UL_key), decod(i['pass'], UL_key)

        else:   # если профиль ненайден
            a = input('Профиль не найден.\nНеобходима регестрация?\nДля подтверждения введите [да/yes]\n').lower()
            if a  in ['yes', 'да']:
                login = input('Введи логин от профиля!\n')
                password = input('Введи пароль от профиля!\n')
                writer = csv.writer(prof, delimiter=';')
                writer.writerow([SES(str(login), UL_key), SES(str(password), UL_key), SES(str(UL_key), UL_key)])
                return login, password
            else:
                return users()

def ru_en_translate(txt):
    lang = {"А":'A', "Б":'B', "В":'V', "Г":'G', "Д":'D', "Е":'E', "Ж":'ZH', "З":'Z', "И":'I', "Й":'J', "К":'K', "Л":'L', "М":'M', "Н":'N', "О":'O', "П":'P', "Р":'R', "С":'S', "Т":'T', "У":'U', "Ф":'F', "Х":'H', "Ц":'TS', "Ч":'CH', "Ш":'SH', "Щ":'SHCH', "Ъ":'', "Ы":'Y', "Ь":'', "Э":'E', "Ю":'YA', "Я":'YA', ' ':' '}
    sl = ''
    for i in txt.upper():
        if i in lang: sl += lang[i]
        else: continue 
    return sl.lower().title()

def SES(sl, UL_key): 
    txt = list(map(lambda a: int(hex(ord(a)+UL_key), 16) ,sl))
    return ' '.join(map(str, txt))

def decod(sl, UL_key):
    txt = list(map(int, sl.split()))
    return ''.join(list(map(lambda a: chr(int(str(a-UL_key), 10)) ,txt)))

def grup(txt):
    x1 = [k for k in txt]
    #x2 = input('Введи код посещения:') # 0121301300210 **********************************************************
    for k in range(len(x1)):
        txt[x1[k]].append(x2[k])
    return txt

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
            general_c += random.choice(sl)  + ' Так же надо заметить: '
        way2 = pathlib.Path(find_file('nch2.csv'))
        with way2.open('r', encoding='utf-8') as path:
            sl = list(map( lambda a: a[-1], list(csv.reader(path, delimiter=';'))))[1:]
            general_c += random.choice(sl) + ' Что бы усваивать материал более качественно рекомендую: '
        way3 = pathlib.Path(find_file('nch3.csv'))
        with way3.open('r', encoding='utf-8') as path:
            sl = list(map( lambda a: a[-1], list(csv.reader(path, delimiter=';'))))[1:]
            general_c += random.choice(sl) + '<----'
        if 'Мужчина' in x: general_c = f'ученика был на {x[2]} уроках. За эти 3 дня: ---->' + general_c
        else: general_c = f'ученика была на {x[2]} уроках. За эти 3 дня:' + general_c
    else: general_c += 'Н.Б'
    x.append(general_c)
    return x

def creating_templates(txt):
    txt1 = list(filter(lambda a: True if len([1 for i in a if str(i).isdigit()])!=0 else False ,txt))
    txt1 = list(map(lambda x: CHupp(x) , txt1))
    txt1 = list(map( lambda a: [*a[:-1], a[-1].replace('ученика', a[0].split()[-1])], txt1)) # ребенка, ученику
    txt1 = list(map( lambda a: [*a[:-1], a[-1].replace('ребенка', 'ученика')], txt1))
    txt1 = list(map( lambda a: [*a[:-1], a[-1].replace('ребенку', 'ученику')], txt1))
    #txt1 = list(map( lambda a: [*a[:-1], a[-1].replace('ученику', a[0].split()[-1])], txt1))
    return txt1

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

def pol(txt):
    a = txt.split()
    if a[0][-1] == 'а' or a[-1][-1] in ['а', "я"]: return 'Девушка'
    else: return 'Мужчина'