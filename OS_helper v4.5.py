from funk import *
import datetime
#************************************** ОСНОВНОЙ ЦИКЛ КОДА **************************************

#************************************** ЭТАП 1 **************************************

login, password = users()

while True:
    url = input('Введите url адрес группы.\n')

    students, visits, name_group = zapros_url(url, login, password)

    txt = gender(students, visits)

    #************************************** ЭТАП 3 **************************************
    way = pathlib.Path(find_file('os_group.tsv')).resolve()
    with way.open('a', encoding='utf-8') as lib:
        ts = creating_templates(txt)
        print(f"Группа: {date.today()- timedelta(3)}", '\t'+str(*name_group), file=lib)
        for k in ts:
            print(k[0]+'\t', k[-1], file=lib)
        print('****************************************************************************', file=lib)
        print('Данные сохранены в текстовый файл os_group', f'Путь сохронения: {way}', sep='\n')
    void_loop = input('Для завершения введите [stop / x / хватит]\n').lower() 
    if void_loop != 'хватит' or void_loop != 'x' or void_loop != 'stop': break

