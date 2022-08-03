#empty_dict = {}
# language = {'name':'Python',
#         'version':3.8,
#}#
# dict1={
#     1:2,
#     'str':'string',
#     'bool':True,
#     'list':[1,2,3],
# }

# dict2= dict(name='name',age='age',height='height')
# print(dict2)
#print(dict1)


# person={
#     'name':'John Smith',
#     'age':30,
#     'profession':'Python def'
# }person={}




# person2 = {'race': 'ork'}
# person.update(person2)
# person.pop('age')# удаляет по ключу
# print(person.get('race'))
# print(person)
# print(person['name'])
# person.clear()# очищает словарь
# a = person.copy()# копирует словарь
# person.setdefault(7, 'seven')#Создает новую пару ключ-значение,но если такой ключ уже есть, ничего не произойдет
# print(person.values())
# print(person.keys())
# print(person.items())

# nm['name']='Rikki'
# nm['age']=18
# nm['planet']='earth'
# nm2={'race':'negr'}
# nm.update(nm2)
# nm.pop('age')

# a = set()
# b=10
# c =12 
# d= True
# a.add(b)
# a.add(c)
# a.add(d)
# print(a)






# set_1 = {1,2,3,4,5,5,5,5,6,7,8,9}
#print(set_1)
# set_1.clear
# print(set_1)



# set1={'Toma','Arsen','Bob','Mars','Tim'}
# set2={'Arsen','Toma','Bob','fvgfj','gyufg'}
# set3=set2.difference(set1)
# print(set3)


# a={1,2,3}
# b = {4,5,6}
# a.update(b)
# a.remove(1)
# print(a)




# a = {1,2,3,4,5}
# b = {1,2,3,7,8,9}
# c = a.intersection(b)
# print(c)



# a ={
#     'number':[4,7,8]
# }

# for value in a.values():
#     print(value[0])





# # Практические задания: Множества и Словари
# ################################################################################
 
# # Множество № 1:
#dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}


 
# # Список № 2
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
#    'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# south_american_countries.remove('Suriname')
# print(south_american_countries)
 
# # # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
 
# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# c=farm_2.difference(farm_1)
# print(c)
 
# # Словарь №1:
#menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu2 = {'besh_barmak': 130}
# menu.update(menu2)
# menu['lagman']= 135
# menu.pop('borsh')
# print(menu)
# a={'drinks':['Coca-Cola','Sprite','Fanta']}
# menu.update(a)
# print(menu)



# dict = {'Katte':'teacher','Roma':'builder','Tima':'student','Milana':'nanny','Bob':'taxi driver'}
# for i in dict:
#     dict=input(' здравствуйте имя:')
#     if i in dict:
#         print('прекрастная профессия')


    

# person = {
#     'name': 'John Smith',
#     'age': 30,
#     'profession': 'Python dev'
# }
# for key, value in person.items():
#     print(f'{key} = {value}')




# suitcase=['phone','krem ot zagara','maney','key','comp']
# suitcase.remove('comp')
# print(suitcase)












