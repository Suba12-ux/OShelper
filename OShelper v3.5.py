def vvod():
	txt = []
	sl = ''
	while sl != 'stop':
		sl = input()
		if sl.isspace() or sl == '':
			continue
		else:
			txt.append(sl)
	txt2 = []
	for i in txt:
		if i.split()[-1].isalpha() and i != 'stop':
			txt2.append(i)
		else:
			continue
	return txt2

def keyser(txt):
	x1 = [k for k in txt]
	return x1

def xar():
    import random
    sl1 = {'5':'Ваня — настоящий маленький энерджайзер на уроке! постоянно в движении: задаёт вопросы, поднимает руку, чтобы ответить, участвует в обсуждениях. Иногда кажется, что не может усидеть на месте ни минуты. Но активность не мешает остальным ученикам, а, наоборот, заряжает их позитивом и энтузиазмом.', 
    '4': 'Ваня легко усваивает новый материал и хорошо справляется с заданиями. Помогает одноклассникам разобраться в сложных темах и всегда делится своими знаниями.',
    '3': 'Ваня может потребоваться дополнительная мотивация, чтобы лучше усвоить материал. Может помочь интересные задания или проекты. Не всегда поднимает руку.',
    '2': 'Ваня спокойно выполняет задания, но иногда может нуждаться в дополнительной поддержке и мотивации.',
    '1': 'Ваня спокойно выполняет задания, но иногда может нуждаться в дополнительной поддержке и мотивации.',
    '7': 'Ученик демонстрирует высокую активность на онлайн-уроках. Он активно задаёт вопросы по теме, активно участвует в обсуждениях и старательно выполняет задания преподавателя. Проявляет стремление к глубокому пониманию материала и не боится выражать свои мысли и мнения.',
    '8': 'Как ученик проявляет активность на онлайн-уроках?\n 	- Ученик задаёт вопросы, когда что-то непонятно, и участвует в обсуждениях.\n О чём свидетельствует высокая активность ученика на уроках?\n 	- Высокая активность ученика на уроках свидетельствует о его заинтересованности в предмете и стремлении к пониманию материала.',
    '9': 'Активность ученика на онлайн-уроках проявляется в его готовности задавать вопросы, участвовать в обсуждениях и проявлять интерес к предмету. Высокая активность свидетельствует о заинтересованности ученика в понимании материала и его стремлении получить знания.',
    '10':'Вовлеченность ученика на онлайн-уроках проявляется в его готовности задавать вопросы, активно участвовать в обсуждениях и проявлять живой интерес к изучаемому предмету. Высокая степень вовлеченности свидетельствует о глубоком интересе ученика к пониманию материала и его стремлении к получению знаний.',
    '6': 'Ученик проявляет высокую активность на онлайн-уроках. Он задаёт вопросы по теме, участвует в обсуждениях и выполняет задания преподавателя. Стремится к глубокому пониманию материала и не боится высказывать своё мнение.'}
    sl2 = {'5': 'Ваня активно участвует в обсуждениях, внимательно слушает учителя и старательно выполняет задания. Не боится высказывать своё мнение и задавать вопросы, если что-то непонятно.',
    '4': 'Ваня в целом сосредоточен на заданиях и старается выполнять их качественно. Однако иногда может отвлекаться, поэтому требуется дополнительная поддержка и мотивация.',
    '3': 'Ваня может испытывать трудности с концентрацией, проявлять признаки беспокойства или неуверенности.',
    '2': 'Ваня демонстрирует отличные результаты, сосредоточен на заданиях и выполняет их с большим усердием. Проявляет признаки уверенности и интереса. Создает максимально спокойной обстановки на уроке.',
    '1': 'Ваня в целом сосредоточен на заданиях и старается выполнять их качественно. Однако иногда может отвлекаться, поэтому требуется дополнительная поддержка и мотивация.',
    '6': 'На онлайн-уроках ученик демонстрирует хорошую успеваемость, активно участвует в обсуждениях и задаёт вопросы по теме. Проявляет живой интерес к изучаемому предмету и стремится к получению знаний.',
    '7': 'На онлайн-уроках ученик демонстрирует средний результат. Он участвует в обсуждениях и иногда задаёт вопросы по теме. Его интерес к предмету и стремление к знаниям очевидны, но не всегда ярко выражены.',
    '8': 'На онлайн-уроках ученик показывает средние результаты. Он активно участвует в обсуждениях и иногда задаёт вопросы по теме. Его интерес к предмету и стремление к знаниям видны, но не всегда ярко выражены.',
    '9': 'Этот ученик на онлайн-уроках показывает средние результаты. Он активно участвует в обсуждениях и иногда задаёт вопросы по теме. Хотя его интерес к предмету и стремление к знаниям заметны, они не всегда проявляются в полной мере.',
    '10':'На онлайн-уроках этот учащийся демонстрирует средние результаты. Он активно участвует в обсуждениях и иногда задаёт вопросы по теме. Хотя его интерес к предмету и стремление к знаниям очевидны, они не всегда проявляются в полной мере.'}
    sl3 = {'5':'Ученик испытывает определённые трудности с концентрацией на заданиях, поэтому требуется дополнительная поддержка и мотивация со стороны учителя. Важно создать условия, в которых сможет максимально сосредоточиться на уроке.',
    '4': 'Уровень затруднения на уроках можно оценить как средний. Ученик старается выполнять задания качественно, но иногда отвлекается.',
    '3': 'Ученик иногда отвлекается и не может полностью сосредоточиться на заданиях. Требуется дополнительная поддержка и мотивация, чтобы помочь преодолеть эти трудности и достичь лучших результатов.',
    '2': 'Ученик демонстрирует хорошие результаты и редко испытывает затруднения на уроках. внимательно слушает учителя, старается выполнять задания качественно и не отвлекается. Это говорит об ответственности и усердии.',
    '1': 'Ученик сосредоточен на заданиях и редко отвлекается. проявляет признаки уверенности и интереса, что говорит об успешном освоении материала. Важно продолжать поддерживать мотивацию и интерес к предмету.',
    '6': 'Этот ученик показывает стабильные результаты на онлайн-уроках, активно участвует в обсуждениях и иногда задаёт глубокие и содержательные вопросы по теме. Его интерес к предмету и стремление к знаниям очевидны и заслуживают высокой оценки.',
    '7': 'Этот ученик демонстрирует отличные результаты на онлайн-уроках, активно участвует в обсуждениях и иногда поднимает глубокие и интересные вопросы по теме. Его увлеченность предметом и стремление к знаниям видны невооруженным глазом и заслуживают высокой оценки.',
    '8': 'Ученик показывает превосходные результаты на онлайн-уроках, активно участвует в обсуждениях и иногда поднимает глубокие и интересные вопросы по теме. Его страсть к предмету и стремление к знаниям очевидны и заслуживают высокой оценки.',
    '9': 'Этот ученик не показывает превосходных результатов на онлайн-уроках, редко участвует в обсуждениях и не поднимает глубокие и захватывающие вопросы по теме. Его страсть к предмету и стремление к знаниям отсутствуют и заслуживают низкой оценки.',
    '10': 'Этот ученик не показывает превосходные результаты на онлайн-уроках, редко участвует в обсуждениях и не поднимает глубокие и интересные вопросы по теме. Его страсть к предмету и стремление к знаниям не очевидны и заслуживают низкой оценки.'}
    sl4 = {'1': 'Проблем с коммуникацией не возникало.',
    '2': 'Небольшие проблемы с коммуникацией.',
    '3': 'Заметил что предпочитает избегать общения как со сверстниками, так и с преподователем.',
    '4': 'Проблем с коммуникацией не возникало.',
    '5': 'Проблем с коммуникацией не возникало.'}
    sl5 = {'1':'Стоит проработать задания более вдумчиво что бы закрепить знания',
    '2': 'Чтобы лучше усвоить материал, постарайтесь выполнять задания тщательно и вдумчиво.',
    '3': 'Для более глубокого понимания и запоминания материала рекомендуется выполнять задания тщательно и вдумчиво. Это поможет вам лучше разобраться в теме и применить полученные знания на практике.',
    '4': 'Кроме того, регулярное повторение материала и интеграция в повседневную жизнь помогают лучше усваивать информацию.',
    '5': 'Дополнительно, можно использовать мнемонические техники для запоминания информации. Например, создание ассоциаций, использование рифм или создание визуальных образов.',
    '6': 'Для лучшего усвоения материала, старайтесь выполнять задания внимательно и с полным пониманием.',
    '7': 'Чтобы материал лучше усвоился, выполняйте задания аккуратно и вдумчиво.',
    '8': 'Чтобы материал закрепился в памяти, старайтесь выполнять задания тщательно и с полной концентрацией.',
    '9': 'Для более глубокого понимания, выполняйте задания внимательно и вдумчиво.',
    '10': 'Чтобы материал усвоился, старайтесь выполнять задания тщательно и с полным погружением.',
    '11': 'Чтобы лучше усвоить материал, выполняйте задания с таким интересом и вниманием, как археолог, который ищет древние артефакты. Представьте, что каждое задание — это ключ к разгадке тайн, и раскройте его внимательно и тщательно, как детектив, который расследует сложное дело.',
    '12': 'Чтобы материал хорошо запомнился, выполняйте задания аккуратно и тщательно, как ювелир, который ограняет драгоценные камни знаний. Погрузитесь в процесс так же, как музыкант, который настраивает инструмент перед концертом, чтобы каждое задание звучало гармонично в вашей голове.',
    '13': 'Для более глубокого понимания материала выполняйте задания с энтузиазмом, как исследователь, который открывает новые земли. Пусть каждый вопрос станет для вас вызовом, который вы с удовольствием принимаете, и пусть ваше стремление к знаниям будет безграничным, как океан, полный неизведанных глубин.',
    '14': 'Чтобы материал запомнился надолго, выполняйте задания с аккуратностью и вниманием, словно ювелир, который обрабатывает драгоценные камни знаний. Погрузитесь в процесс, как музыкант, настраивающий инструмент перед концертом, и каждое задание будет звучать в вашей голове с удивительной гармонией.'}
    txt = [sl1, sl2, sl3, sl4, sl5]
    txt2 = ''
    import random
    for i in txt:
    	h1 = keyser(i)
    	txt2 += i[random.choice(h1)] #+'\t'
    return txt2

def grup(txt):
	x1 = txt
	x2 = input('Введи код посещения:') # 0121301300210 **********************************************************
	txt0 = {}
	txt1 = {}
	txt2 = {}
	txt3 = {}
	for i in x1:
		if x2[x1.index(i)] == '3':	
			txt3.setdefault(i, [x2[x1.index(i)]])
		elif x2[x1.index(i)] == '2':
			txt2.setdefault(i, [x2[x1.index(i)]])
		elif x2[x1.index(i)] == '1':
			txt1.setdefault(i, [x2[x1.index(i)]])
		elif x2[x1.index(i)] == '0':
			txt0.setdefault(i, [x2[x1.index(i)]])
	gr = [txt0, txt1, txt2, txt3]
	return gr

def appxar(txt):
	x1 = txt
	for k in x1:
		for j in k:
			if '3' in k[j]:
				k[j].append(f'{j} был(а) на 3 уроках.'+ xar())
			elif '2' in k[j]:
				k[j].append(f'{j} был(а) на 2 уроках.' + xar())
			elif '1' in k[j]:
				k[j].append(f'{j} был(а) на 1 уроках.')	
			else:
				k[j].append('Н.Б')
	return x1


# осовной цикл прогрммы ************************************************************************************

print('Введи спиок группы:')
txt = vvod() 							# stop команда для остановки ввода.************************************************************
txt2 = grup(txt) 						# 0121301300210 ***************************************************************************
x0, x1, x2, x3  = appxar(txt2)

for k in x3:
	x3[k][-1] = x3[k][-1].replace('Ваня', k.split()[-1])
	x3[k][-1] = x3[k][-1].replace('Ученик', k.split()[-1])
	x3[k][-1] = x3[k][-1].replace('Он ', k.split()[-1])
	x3[k][-1] = x3[k][-1].replace(' он ', '')
	x3[k][-1] = x3[k][-1].replace('его ', '')
	x3[k][-1] = x3[k][-1].replace('Его ', '')
	x3[k][-1] = x3[k][-1].replace('этот ', '')
	x3[k][-1] = x3[k][-1].replace('Этот ', '')
for k in x2:
	x2[k][-1] = x2[k][-1].replace('Ваня', k.split()[-1])
	x2[k][-1] = x2[k][-1].replace('Ученик', k.split()[-1])
	x2[k][-1] = x2[k][-1].replace('Он ', k.split()[-1])
	x2[k][-1] = x2[k][-1].replace(' он ', '')
	x2[k][-1] = x2[k][-1].replace(' его ', '')
	x2[k][-1] = x2[k][-1].replace('Его ', '')
	x2[k][-1] = x2[k][-1].replace(' этот ', '')
	x2[k][-1] = x2[k][-1].replace('Этот ', '')

print('0 ПОСЕЩЕНИЯ ******************************************************************************************************')

for k in x0:
	print(k, x0[k][-1], sep='\t')

print('1 ПОСЕЩЕНИЯ ***********************')
for k in x1:
	print(k, x1[k][-1], sep='\t')

print('2 ПОСЕЩЕНИЯ ***********************')
for k in x2:
	print(k, x2[k][-1], sep='\t')

print('3 ПОСЕЩЕНИЯ ***********************')
for k in x3:
	print(k, x3[k][-1], sep='\t')

print('******************************************************************************************************')