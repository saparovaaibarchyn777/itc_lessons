# users = {
#     'Admin':{
#         'name':'admin',
#         'phone':'996708675645',
#         'balance':50000,
#         'password':'12312321'
#     },
#     'Amina':{
#         'name':'Amina',
#         'phone':'996708340678',
#         'balance':500,
#         'password':'12312321'

#     }
# }
# key=None
# while True:
#     if key is  None:
#         print('Здравствуйте уважаемый клиент')
#         m=int(input('''
#         1 Зарегистрироваться
#         2 Авторизоваться
#         3 Перевод баланса
#         4 Список пользователей
#         5 Информация
#         6 Выход из банка
#         >>>'''))
#         if m == 1:
#             login = input('Введите логин:')
#             name = input ('Введите ваше имя:')
#             phone = input('Введите ваш номер +996')
#             password = input('Придумайте пароль:')
#             password1 = input('Подтвердите  пароль:')
#             while password == password1 and len(password)<8:
#                 password = input('Ваш пароль не совпадает или меньше 8 символов\<<< ')
#                 password1 = input('Повторите пароль')
#             else:
#                 users.update({
#                     login:{
#                         'name':name,
#                         'phone':phone,
#                         'balance':1000,
#                         'password':password
#                     }
#                 })
#                 print('Регистрация успешна')
#                 key = login
#             if m == 2:
#                 if key is None :
#                     print('Добро пожаловать в авторизацию ')
#                     login = input('Введите логин')
#                     password = input('Введите пароль')
#                     if login is users:
#                         if password==users[login][password]:
#                             print('Вы авторизовались')
#                             key = login
#                         else:
#                             print('Не верный пароль')
#                     else:
#                         print('Нет такого пользователя')
#                 else:
#                     print('Вы уже авторизованы')
#                 if m==3 :
#                     if users is not None:
#                         loginP = input('Введите имя пользователя')
#                         summa = int(input('Введите сумму перевода'))
#                         if loginP in users:
#                             if summa <=users [key]['balance']:
#                                 users[key]['balance']-=summa
#                                 users[loginP]['balance']
#                                 print('перевод успешен')
#                             else:
#                                 print('У вас не достаточно денег')
#                         else:
#                             print('Такого пользователя нет')
#                     else:
#                         print('Вы не авторизованы')
#                 if m ==4:
#                     print(users)
#                 if m ==5:
#                     print(f'''
#                     Логин:{users["Admin"]}
#                     Имя :{users["Admin"]['phone']}
#                     Номер телефона:{users["Admin"]['phone']}
#                     Баланс:{users["Admin"]['balance']}
#                     ''')
                    
                    

#                     if m ==6:
#                         print('Приходите еще')
#                         break
                    



# users = {
#     'Admin':{
#         'name':'admin',
#         'phone':'996555444333',
#         'balance':500000,
#         'password':'12312321'
#     },
#     'Argen':{
#         'name':'Argen',
#         'phone':'999580780',
#         'balance':5000,
#         'password':'12312321'
#     }
# }
# key = None
# while True:
#     print('Здраствуйте уважаемый клиент!')
#     m = int(input('''
#     1 Заарегистрироваться 
#     2 Авторизоваться 
#     3 Перевод баланса
#     4 Список пользователей 
#     5 Информатция 
#     6 Изменить логин
#     7 Изменить пароль
#     8 Выход из банка
#     >>> '''))
#     if m == 1:
#         if key is None:
#             login = input('введите логин ')
#             name = input('введите полное ваше имя ')
#             phone = int(input('введите ваш номер +996'))
#             password = input('Придумайте пароль ')
#             password1 = input('Подтвердите пароль ')
#             while password != password1 and len(password) < 8:
#                 password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
#                 password1 = input('Повторите пароль ')
#             else:
#                 users.update({
#                     login :{
#                         'name':name,
#                         'phone':phone,
#                         'balance':1000,
#                         'password':password
#                     }
#                 })
#                 print('Регистратция успешна')
#                 key = login
#     elif m == 2:    
#         if key is None:
#             print('Добро пожаловать в авторизатцию ')
#             login = input('Введите логин ')
#             password = input('введите пароль ')
#             if login in users:
#                 if password == users[login]['password']:
#                     print('Вы авторизовались ')
#                     key = login
#                 else:[print('Не верный пароль')]
#             else:[print('Нет такого пользователя ')]
#         else:[print('Вы уже авторизованы ')]
#     elif m == 3:
#         if users is not None:
#             loginP = input('Введите имя получателя ')
#             summa = int(input('введите сумму перевода '))
#             if loginP in users:
#                 if summa <= users[key]['balance']:
#                     users[key]['balance'] -= summa
#                     users[loginP]['balance']+= summa
#                     print('Перевод успешен')
#                 else:[print('У вас не достаточно денег')]
#             else:[print('такого пользователя нет')]
#         else:[print('вы не авторизованы')]
#     elif m == 4:
#         if key is not None:
#             print(users)
#     elif m == 5:
#         if key is not None:[print(f'''
#             Логин: {users["Admin"]}
#             Имя: {users["Admin"]['name']}
#             Номер телефона: {users["Admin"]['phone']}
#             Баланс: {users["Admin"]['balance']}
#             \n''')]
#         else:[print('вы не авторизованы')]
#     elif m == 6:
#         if key is not None:
#             print(f'\nВаш login: {login}\n')
#             new_login = input('Введите новый логин: ')
#             login = new_login
#             print(f'Логин успешно обновлён на {login}')
#         else:[print('вы не авторизованы')]
#     elif m == 7:
#         if key is not None:
#             print(f'\nВаш пароль: {users["Admin"]["password"]}\n')
#             password = input('Введите текуший пароль: ')
#             if password == users[key]['password']:
#                 password = input('Введите новый пароль: ')
#                 password1 = input('Подтвердите новый пароль: ')
#                 while password != password1 and len(password) < 8:
#                     password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
#                     password1 = input('Подтвердите новый пароль ')
#                 else:[users.update({
#                         login :{
#                             'name':name,
#                             'phone':phone,
#                             'balance':1000,
#                             'password':password
#                         }
#                     })]
#             else:[print('Извините пароль не верный')]
#         else:[print('вы не авторизованы')]
#     elif m == 8:
#             print('Приходите ещё ')
#             break
#     else:[print('Брат такой команды нет')]





# d = {
#     '1':3,
#     'true':True,
#     'list':[1,2,3],
#     'name':{'Bob':'+77 555 999',
#     'Nicky':'+77 888 998',
#     'Nicky Wittle':'+77 99 000'}
# }
#print(d['name']['Nicky'])
# for key in d:
#     for i in key :
#         print(i)




# new_login = input('Введите новый логин: ')
#             f = open('База вашего банка.txt','a+')
#             f.write(f'\nУзер {login} Изменил свой логин на {new_login}\n') 
#             f.close()
#             login = new_login
#             print(f'Логин успешно обновлён на {login}')
#         else:[print('вы не авторизованы')]
#     elif m == 7:
#         if key is not None:
#             print(f'\nВаш пароль: {users["Admin"]["password"]}\n')
#             password = input('Введите текуший пароль: ')
#             if password == users[key]['password']:
#                 print('Пароль должен быть не менее 8 сиволов \n')
#                 password = input('Введите новый пароль: ')
#                 password1 = input('Подтвердите новый пароль: ')
#                 f = open('База вашего банка.txt','a+')
#                 f.write(f'\nУзер {key} изменил свой пароль на {users[login]["password"]}\n') 
#                 f.close()
#                 while password != password1 and len(password) < 8:
#                     password = input('Ваш паролль не совподает или она меньше 8 символов \n>>>')
#                     password1 = input('Подтвердите новый пароль ')
#                 else:
#                     users.update({
#                         login :{
#                             'name':name,
#                             'phone':phone,
#                             'balance':1000,
#                             'password':password
#                         }
#                     })
#                     f = open('База вашего банка.txt','a+')
#                     f.write(f'\nУзер {key} изменил свой пароль на {users[login]["password"]}\n')
#                     f.close()
#             else:[print('Извините пароль не верный')]
#         else:[print('вы не авторизованы')]  
#     elif m == 8:
#         print('Приходите ещё ')
#         break
#     else:[print('Брат такой команды нет')]



# a = input('''
#     1 *
#     2 /
#     3 + 
#     4 -
#     5 //
#     6 **
#     7 % 
#     >>> ''')
# if a == 1:
#     b = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     print(f'результат: {b * c}')
# elif a == 2:
#     b = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     print(f'результат: {b / c}')
# elif a == 3:
#     b = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     print(f'результат: {b + c}')
# elif a == 4:
#     b = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     print(f'результат: {b - c}')
# elif a == 5:
#     b = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     print(f'результат: {b // c}')
# elif a == 6:
#     b = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     print(f'результат: {b ** c}')
# elif a == 7:
#     b = int(input('Введите первое число: '))
#     c = int(input('Введите второе число: '))
#     print(f'результат: {b % c}')
# else:
#     print('Извините такой команды нет!')

#'Задание №4': """
#             Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
#             Возьмите строку "4729461084" и сложите все её числа.
#             Результат выведите на экран.""",
 
 #zadanie 2 tascs1
# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 89]
# a.append(13)
# b = a.count(13)
# v = len(a)
# s = b * 100 / v
# print(s)

# if s< 70:
#     print('Неужели')
# elif s >70:
#         print('Я так и знал')
# else:
#             print('Cовподение? Не думаю')   
