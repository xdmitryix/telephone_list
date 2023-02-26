import json

telephone_sp= [
                {'фамилия': 'Петров', 'имя': 'Петр', 'отчество': 'Петрович', 'телефон': '89567378844'},
                {'фамилия': 'Иванов', 'имя': 'Иван', 'отчество': 'Иванович', 'телефон': '89445678900'},
                {'фамилия': 'Васильев', 'имя': 'Василий', 'отчество': 'Васильевич', 'телефон': '89564468909'},
                ]


def save():
    with open("telephone_sp.json","w", encoding="utf-8") as ts:
        ts.write(json.dumps(telephone_sp,ensure_ascii=False))
    print("Ваш телефонный справочник был успешно сохранен в файле telephone_sp.json")

def add_list(data_list):
    f = input('введите фамилию нового контакта: ')
    i = input('введите имя нового контакта: ')
    o = input('введите отчество нового контакта: ')
    t = input('введите номер телефона нового контакта: ')
    data_list.append({'фамилия': f, 'имя': i, 'отчество': o, 'телефон': t})

def delete_list(data_list):
    res = []
    text = input('введите данные удаляемого контакта: ')
    for i in data_list:  
        if i['фамилия'] == text:
            res.append(i)
        elif i['имя'] == text:
            res.append(i)
        elif i['отчество'] == text:
            res.append(i)
        elif i['телефон'] == text:
            res.append(i)
    if len(res) < 1:
        print('пользователя нет в списке контактов.')
    elif len(res) == 1:
        temp = 0 
        for k in data_list:
            for l in res:
                if k == l:
                    del data_list[temp]
                temp = temp + 1 
        print('Контакт успешно удален из справочника!')
    else:
        temp_nums = 0
        print('В справочнике нашлось', len(res) , 'котнакта подхожящих под кретерий поиска:')
        print(res)
        num = input('Для корректного удаления нужного контакта воспользуйтесь поиском по номеру телефона! Введите номер удаляемого контакта: ')
        for m in data_list:
            if m['телефон'] == num:
                del data_list[temp_nums]
                print('контакт успешно удален из списка !')
            temp_nums = temp_nums+1
            

def search_list(data_list):
    res = []
    text = input('введите данные искомого контакта: ')
    flag = False
    for i in data_list:     
        if i['фамилия'] == text:
            print(i)
            flag = True
        elif i['имя'] == text:
            print(i)
            flag = True 
        elif i['отчество'] == text:
            print(i)
            flag = True 
        elif i['телефон'] == text:
            print(i)
            flag = True 
    if flag == False:
        print('контакт отсутствует в списке.')




print('Добро пожаловать в телефонный справочник! Введите /help для просмотра мануала')
while True:
    command = input('Введи команду:\n')
    if command == '/start':
        print('Бот начал работу !')
    elif command == '/help':
        print ('Введи команду:\n /help - справка\n /start - начало чата\n /stop - остановить бот\n \
/all - выведи весь список контактов\n /add - добавить новый контакт\n /del - удалить контакт из справочника\n /save - сохранение данных\n /load - загрузка данных\n \
/sear - поиск контакта\n')
    elif command == '/stop':
        save()
        print('Бот остановил свою работу.')
        break
    elif command == '/all':
        print('Весь список контактов:')
        print(telephone_sp)
    elif command == '/add':
        add_list(telephone_sp)
        print('контакт успешно добавлен в справочник!')
    elif command == '/del':
        delete_list(telephone_sp)
    elif command == '/save':
        save()
    elif command == '/load':
        with open("telephone_sp.json","r", encoding="utf-8") as ts:
            telephone_sp = json.load(ts)
        print("Ваш телефонный справочник был успешно загружен из файла telephone_sp.json")
    elif command == '/sear':
        search_list(telephone_sp)
    else:
        print("Неопознанная команда. Просьба изучить мануал через команду /help")



    # elif command == '/find':
    #     find_data = input('Введите искомые данные:')
    #     for k,v in telephone_sp.items():
    #         if find_data in telephone_sp[k,v]:
    #             print(k,v)
            
