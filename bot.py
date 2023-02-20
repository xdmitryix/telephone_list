import json

telephone_sp = {'Иванов Иван Иванович': '89274678934', 'Петров Петр Петрович': '83427773432', 'Федоров Федор Федорович': '82227553678'}



print('Добро пожаловать в телефонный справочник!')
while True:
    command = input('Введи команду:\n')
    if command == '/start':
        print('Бот начал работу !')
    elif command == '/help':
        print ('Введи команду:\n /help - справка\n /start - начало чата\n /quit - выход\n /add - добавить контакт\n /delete - удалить контакт\n /stop - остановить бот\n \
/all - выведи весь список контактов\n')
    elif command == '/stop':
        print('Бот остановил свою работу.')
        break
    elif command == '/all':
        print('Весь список контактов:')
        print(telephone_sp)
    elif command == '/find':
        find_data = input('Введите искомые данные:')
        for k,v in telephone_sp.items():
            if find_data in telephone_sp[k,v]:
                print(k,v)
            
