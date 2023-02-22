import json

telephone_sp = {}
telephone_sp["Иванов Иван Иванович"] = '89274678934'
telephone_sp["Петров Петр Петрови"] = '83427773432'
telephone_sp["Федоров Федор Федорович"] = '82227553678'


def save():
    with open("telephone_sp.json","w", encoding="utf-8") as ts:
        ts.write(json.dumps(telephone_sp,ensure_ascii=False))
    print("Ваш телефонный справочник был успешно сохранен в файле telephone_sp.json")

def add_list(data_list):
    it = iter(input('Введите ФИО и номер телефона через ":" ').split(':'))
    data_list.update(dict(zip(it, it)))

def delete_list(data_list):
    d = input('Введите ФИО удаляемого контакта: ')
    if d in data_list:
        del data_list[d]
        print('контакт успешно удален из справочника!')
    else:
        print('контакт не найден в списке.')




print('Добро пожаловать в телефонный справочник! Введите /help для просмотра мануала')
while True:
    command = input('Введи команду:\n')
    if command == '/start':
        print('Бот начал работу !')
    elif command == '/help':
        print ('Введи команду:\n /help - справка\n /start - начало чата\n /stop - остановить бот\n \
/all - выведи весь список контактов\n /add - добавить новый контакт\n /del - удалить контакт из справочника\n /save - сохранение данных\n /load - загрузка данных\n ')
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
    else:
        print("Неопознанная команда. Просьба изучить мануал через команду /help")



    # elif command == '/find':
    #     find_data = input('Введите искомые данные:')
    #     for k,v in telephone_sp.items():
    #         if find_data in telephone_sp[k,v]:
    #             print(k,v)
            
