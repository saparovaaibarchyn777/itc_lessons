# class Factory:
#     def __init__(self,engines:str, bridges: str) -> None:
#         self.engines = engines 
#         self.bridges = bridges
    
#     def engine(self):
#         return ('Двигатель создан ')
    
#     def bridge(self):
#         return ('Ходовая часть создана')

# n = Factory('camry','xod_chast')

# # n.engine() 
# # n.bridge()

# class Toyota(Factory):
    
#     def wheels(self):
#         return ('Kолеса готовы ')
    

#     def windows(self):
#         return ('Cтекла готовы ')

# a = Toyota('Colesa','Stekla')

# # a.wheels()
# # a.windows()

# r = [n.engine(),n.bridge(),a.wheels(),a.windows()]
# print(r)





# class Zoo:
#     def __init__(self) -> None:
#         self.animal_1 = "Тигр"
#         self.animal_2 = "Бегемот"
#         self.animal_3 = "Жираф"
        
# z = Zoo()
# z.animal_1 = 'Лев'
# z.animal_4 = [z.animal_2,z.animal_3]
# z.animal_3 = 'Змея'
# print(z.animal_1,z.animal_2,z.animal_3,z.animal_4)






# # Задание 1:
# Напишите Программу - которая работает по принципу алгоритма Шифр Цезаря.
# Нужно создать класс состоящий из 2 методов:
# 1. Метод который ШИФРУЕТ данные.
# 2. Метода который ДЕШИФРУЕТ эти же данные.
# Представим что ваш метод получает слово состоящее из ЛЮБЫХ символов.
# Ваш 1-й метод должен вернуть зашифрованную строку.
# Алгоритм Шифрования: ASCII позиция + 7.
# Алгоритм Дешифровки: Обратная операция Алгоритма Шифрования.




# Задание 2
# Перейдитеиспользуйте набор данных под кодовым названием - user_data.
# Создайте класс который будет принимать эти данные как аргумент.
# 1.Создайте метод genders() который вернёт всё разнообразие полов в типе данных Tuple.
# Example: ("Male", "Female",...)
# 2. Создайте метод get_domain() который возвращает Tuple ДОМЕННЫХ имён электронной почты ВСЕХ пользователей.
# Что такое доменное имя:
# python.itc@gmail.com
# 1. ИМЯ ПОЧТЫ - python.itc
# 2. РАЗДЕЛИТЕЛЬНЫЙ СИМВОЛ - @
# 3. ДОМЕННОЕ ИМЯ - gmail.com



############# 2 
# user_data = [{
#   "id": 1,
#   "first_name": "Humphrey",
#   "last_name": "Wilcox",
#   "email": "hwilcox0@odnoklassniki.ru",
#   "gender": "Male",
#   "ip_address": "80.232.175.95"
# }, {
#   "id": 2,
#   "first_name": "Erhard",
#   "last_name": "Byart",
#   "email": "ebyart1@addthis.com",
#   "gender": "Male",
#   "ip_address": "125.7.237.155"
# }, {
#   "id": 3,
#   "first_name": "Brok",
#   "last_name": "Leiden",
#   "email": "bleiden2@usnews.com",
#   "gender": "Male",
#   "ip_address": "108.201.248.102"
# }, {
#   "id": 4,
#   "first_name": "Gradeigh",
#   "last_name": "Spreckley",
#   "email": "gspreckley3@marriott.com",
#   "gender": "Male",
#   "ip_address": "90.169.195.245"
# }, {
#   "id": 5,
#   "first_name": "Trueman",
#   "last_name": "McArd",
#   "email": "tmcard4@cargocollective.com",
#   "gender": "Male",
#   "ip_address": "249.26.239.198"
# }, {
#   "id": 6,
#   "first_name": "Giacobo",
#   "last_name": "Rishworth",
#   "email": "grishworth5@merriam-webster.com",
#   "gender": "Male",
#   "ip_address": "156.104.68.219"
# }, {
#   "id": 7,
#   "first_name": "Marcia",
#   "last_name": "Burney",
#   "email": "mburney6@gmpg.org",
#   "gender": "Female",
#   "ip_address": "52.104.185.232"
# }, {
#   "id": 8,
#   "first_name": "Court",
#   "last_name": "Haysar",
#   "email": "chaysar7@eepurl.com",
#   "gender": "Hidden",
#   "ip_address": "60.138.180.175"
# }, {
#   "id": 9,
#   "first_name": "Penn",
#   "last_name": "Slatten",
#   "email": "pslatten8@narod.ru",
#   "gender": "Male",
#   "ip_address": "216.91.212.228"
# }, {
#   "id": 10,
#   "first_name": "Rayna",
#   "last_name": "Jacobsson",
#   "email": "rjacobsson9@4shared.com",
#   "gender": "Female",
#   "ip_address": "158.81.126.17"
# }, {
#   "id": 11,
#   "first_name": "Elissa",
#   "last_name": "Milch",
#   "email": "emilcha@ucoz.ru",
#   "gender": "Female",
#   "ip_address": "160.46.17.104"
# }, {
#   "id": 12,
#   "first_name": "Cissiee",
#   "last_name": "Dever",
#   "email": "cdeverb@dailymail.co.uk",
#   "gender": "Hidden",
#   "ip_address": "198.12.171.92"
# }, {
#   "id": 13,
#   "first_name": "Lorie",
#   "last_name": "Cavozzi",
#   "email": "lcavozzic@apache.org",
#   "gender": "Female",
#   "ip_address": "252.228.114.151"
# }, {
#   "id": 14,
#   "first_name": "Shelton",
#   "last_name": "Pipe",
#   "email": "spiped@opera.com",
#   "gender": "Male",
#   "ip_address": "217.193.203.141"
# }, {
#   "id": 15,
#   "first_name": "Cordell",
#   "last_name": "Hrinchenko",
#   "email": "chrinchenkoe@ovh.net",
#   "gender": "Transgender",
#   "ip_address": "147.76.167.191"
# }, {
#   "id": 16,
#   "first_name": "Dyanna",
#   "last_name": "Sizzey",
#   "email": "dsizzeyf@xing.com",
#   "gender": "Female",
#   "ip_address": "8.177.20.12"
# }, {
#   "id": 17,
#   "first_name": "Felice",
#   "last_name": "Floyed",
#   "email": "ffloyedg@instagram.com",
#   "gender": "Male",
#   "ip_address": "4.150.254.58"
# }, {
#   "id": 18,
#   "first_name": "Arel",
#   "last_name": "Donoher",
#   "email": "adonoherh@youtu.be",
#   "gender": "Male",
#   "ip_address": "186.214.243.230"
# }, {
#   "id": 19,
#   "first_name": "Kristoffer",
#   "last_name": "Carvill",
#   "email": "kcarvilli@xinhuanet.com",
#   "gender": "Male",
#   "ip_address": "58.204.72.103"
# }, {
#   "id": 20,
#   "first_name": "Norbie",
#   "last_name": "Oleksinski",
#   "email": "noleksinskij@free.fr",
#   "gender": "Male",
#   "ip_address": "242.192.49.216"
# }]

# class Data(object):
#     def __init__(self, user_data: dict) -> None:
#         self.user_data = user_data

#     def get_data(self, data: str) -> tuple:
#         items = []
#         for user in self.user_data:
#             for key, value in user.items():
#                 if key == data:
#                     items.append(value)
#         return tuple(items) 

############ 1 

# class Sezar:
#     def shifr(s,n):
#         if s > 26:
#             s = s%26
#         caesar=''
#         for i in n.upper():
#             if ord(i) >= ord('a') and ord(i) <= ord('z'):
#                 if ord(i)+s>ord('z'):
#                     caesar = caesar+chr((ord(i)+s)-26)
#                 else:
#                     caesar=caesar+chr(ord(i)+s)
#             else:
#                 caesar=caesar+i
#         return caesar

#     def dishifr(s,n):
#         if s > 26:
#             s = s%26
#         caesar = ''
#         for i in n:
#             if ord(i)>=ord('a') and ord(i) <= ord('z'):
#                 if ord(i)-s<ord('a'):
#                     caesar = caesar+chr((ord(i)-s)+26)
#                 else:
#                     caesar = caesar+chr(ord(i)-s)
            
#             else:
#                 caesar = caesar+i
#         return caesar
#     s = input("Введите ключ : ")
#     n = input("Введите текст : ")


#     # print (dishifr(int(s),n))
#     print (shifr(int(s),n))
 
    
    


