# a =list(range(5,50,3))
# print(a)

# import time

# for hour in range(24):
    
#         for minut in range(60):
#             for second in range(60):
#                 print(f'{hour}:{minut}:{second}')
#                 time.sleep(1)
    
#nums = [1,1,2,3,3,4,5,6,7,8,9,9,345,767,968,940,34]
# s = set(nums)
#nums_t = []
# for i in s:
#     if nums.count(i)>1:
        
#         nums_t.append(i,nums.count(i))
# print(nums_t)
# nums_t= [(i,nums.count(i)) for i in set(nums) if nums.count(i)>1]
# print(nums_t)

# # # s = set(a)


#
# if len(a)!= len(s):
#     print('znach povtor')
# else:
#     print('oni unikalny')
# print(a)
# print(s)



# a = {1,2,1,1,1,1,1,}
# print(a)


# a = {
#     ''
# }


# a =[ 1, 2, [3,5,6,7,8,]4,8]
# print (a[2])
# a = {
#     1:1,
#     3:3,
#     'lius':{
#         'tree':3,
#         '4':4,
#         '7':7
#     }
# }
# print(a['lius'['tree']])



# s = {}
# for key ,value in a ['lius'].items():
#     print(key,value)
#     if key == 'tree':
#         s[key]= value
#         print (s.items)



# from re import A


# a = ' hello'
# f = float(a)
# s = str(a)
# b = bool(a)
# l = list(a)
# t = tuple(a)
# #d = dict(a)
# se = set(a)
# print(a)
# print(a)
# print(f)
# print(s)
# print(b)



# a = 564.5
# print(int(a))


# from re import A


# users = {
#     '6575687876':{
#         'name':'Asan',
#         'last_name':'Usonov',
#         'b_year':2000,
#         'gender':'m',
#         'status':False,
#         'ID':'JR55666'

#     }
# }


# users = {
#     '6579099087':{
#         'name':'Uson',
#         'last_name':'Asanov',
#         'b_year':2002,
#         'gender':'m',
#         'status':False,
#         'ID':'JT566898'

#     }
# }
# inn = input('jjj: ')
# name=input('Vvedite name:')
# last_name=input('Vvedite last_name:')
# b_year=input('Vvedite b_year:')
# gender=input(' Vvedite gender:')
# status=input('VVedite status:')
# id=input('Vvedite id:')





# users[inn]={
#     'name':name,
#     'last_name': last_name,
#     'b_year':b_year,
#     'gender':gender,
#     'status':status,
#     'ID':id

# }
# print(users)




# a = 17925
# b = 4394*4
# print(a>b)


# a =8
# n =7
# m = 9
# print(a>n and a<m)


# a = 7
# b = 3
# c = 4,8
# print(a%b*c)


# a = 43+56
# b = 45+6
# print(a!=b)


# a = 768+9845
# b = 5
# print(a*b**2-193432)


# a = 4**5
# b = 512+512
# print(a==b)


# a = -21//10
# print(a)

# a = 2004
# b = 2021
# print(b-a+2)


# a = 17
# b = 100
# print(a/b*100)


# a =3.4
# b =3.9
# c = 3.6
# print(a+b*c)



# a = 4
# b = 9
# c = 2.5
# d = 3
# e = 34
# print(a -e** (b/d)%c)



# a = 2**3
# b = 3**2
# print(a==b)


# a = (1,100)
# if a >= 21:
#     print('razresheno')
# if a <= 57:
#     print('razresheno') 
# else:
#     print('ne razresheno')   



# a = (1,100)
# if a >=21:
#     print('razresheno')
# if a<=57:
#     print('razresheno') 
# else:
#     print('ne razresheno')   



# a = input('vashe imia:')
# print('zdrastvuyte ')
# b = input('vash vozrast:')
# c = input('vash lb film:')
# print('prekrastnyi film')
# print(a , b , c,)



# def print_asan():
#     print('hello')
#     print('world')
#     print('asan')
# print_asan()



# a = [1,2,3,44,3,7,8,9,9,5,6,7,89]
# b = [1,2,3,44,3,7,8,9,9,5,6,7,89]
# def my_len():
#     s = 0
#     for i in a :
#         s += 1
#     print(s)

# my_len()
# my_len()
# def my_len(maasiv):
#     s = 0
#     for i in maasiv:
#         s += 1
#     return s



# a = [1,2,3,44,3,7,8,9,9,5,6,7,89]
# b = [1,2,3,44,3,7,8,6,87,456,9,9,5,6,7,89]
# print(my_len(a))
# print(my_len(b))




# def summ_my(a,b,d):
#     return a +b+d
# s = summ_my(6,8,0)
# print(s)
# while True:
#     input('добро пожаловать на регистрацию')

#     a = input('Введите ваше имя:')
#     b = input('Ваш пароль: ')
#     for i in b:
#         if b != 6:
#             print('пароль не может быть меньше 6 символов')
#         else:
#             print('Вы не зарегистрировались !')

# list1 = ['age','19','name','1']
#####################
# def my_revers(list1):
#     a = list1[:2]
#     b = list1[2:]
#     a.reverse()
#     b.reverse()
#     return a+b
# print(my_revers(list1))


########################

# f = [0,1]
# [f.append(f[-2]+f[-1])
# for i in range(8)]
# print(f)

##########################


# def new_file(file_name):
#     a =input('Vvedite nazvanie file:')
#     import os
#     os.system(f'touch {file_name}.nt')
# new_file('ketti')
# new_file('bob')

##########################
# def gen_number():
#     import random
#     num = '0444'
#     for x in range(6):
#         num = num + random.choice(list('145790'))
#     return num
# print(gen_number())
##########################
# def fibonacci(n):
#     if n in (1,2):
#         return 1
#     return fibonacci(n - 1 )+ fibonacci(n -1)
# print(fibonacci(10))
# fib1=fib2= 1
# n = int(input())
# print(fib1,fib2,end='')
# for i in range(2,n):
    
#     fib1,fib2=fib2, fib1+fib2
#     print(fib1, end=' ')



# lst=list('alan wake')
# print(lst.index('a',0,5))


# def name_3():
#     print('hello world!')
# name_3()
# name_3()
# name_3()


# x = int (input("Vvedite 1 chyslo:"))
# y = int (input("Vvedite 2 chyslo:"))


# def f(a=2):
#     return 2*a -2
# print(f(4))



# z = sum(x,y)    
# print(z)


# print("Hello world! ")
# print("Hello world! ")
# print("Hello world! ")
# print("Hello world! ")


# text = 'sdfgdfg sdfgh sdf'
# text1 = 'world'
# print(text.capitalize())





# spisok = ['a','b','v']

# print(','.join(spisok))

# text = 'ttoottottootto'
# print(text.replace('1','3'))



# massage=67
# print(massage)
# while True:

#     age = int(input('Vvedite vash vozrast\n'))
#     if (age>=25):
#         print('tebe mojno 1 vxodit')
#     elif (age>=18) and (age<25):
#         print('mojno s mom')
#     else:
#         print('tebe nelzia')


# def hello():
#     print('Hello world')
# hello()
# hello()
# hello()
# hello()

# x = int(input('Vvedite 1 chislo:'))
# y = int(input('Vvedite 2 chislo:'))
# a =45
# b = 5
# def f():
#     global a 
#     a = a+2
#     print(a)
# f()
# print(a)


# print(f(2))
# z = summa(x,y)
# print(z)


# a = input('Введи имя брат:')
# b = input('Введи пароль брат:')
# if b !="ITCbootcamp":
#     name=input('Введи имя брат:')
#     number = int(input(':+'))
#     print('\n Пожалуйста',name,'подождите мы отправили сообшение на ваш номер')
#     code=int(input('Введи код братан:'))
#     if code !=5678:
#         print('Неверный код!')
#         code = int(input('Введи код повторно:'))
#         if code !=5678:
#             print('Повтори код через 5 минут!')
#     else:
#         print('Э брат ты авторизован')
# else:
#     print('Э брат ты авторизован')



# name ='Hello world'
# for i in range(1,10):
#     print(name)


# while 1==1:
#     print('Hello world')

# name=[]
# spisok=[1,2,3,4,5,6,7,8,9,90,]
# print(spisok)
# numbers=[1,2,3,4,'name']
# print(numbers)  
# numbers=[12,234,3456] 
# print(numbers)


# from curses.ascii import isalpha, isdigit
# from itertools import tee
# import string
# from unicodedata import name


# #a = input('Vvedi skovo\n')
# # def permute_a_polindrom(input):
#     reversed_input=input[::-1]
#     if input==reversed_input:
#         print(input,'->verno')
#     else:
#         print(input,'->loj')
# permute_a_polindrom('anna')


# def even_or_odd(number):
#     if number %2==0:
#         return 'Even'
#     else:
#         return 'Odd'
    
# def validate_usr(username): 
#     a =input('Vvedi imia')
#     for i in username:
#         if i ==isalpha and isdigit:
#             return True
#         elif i <4 and i >16:
#             return False
#         else:
#             return True
        
# def string_to_number(s):
#     if s==str:
#         s=str(int)
# print(1,2,3,45,67,8,9)
        

# import re
# def validate_usr(username):
#     return bool((re.fullmatch('[a-z_0-9{4,6}',username)))






# def my_fun8(a,b):
#     if x>y:
#             return True
#     return False
# print(my_fun8())
    



# def my_fun7(a,b):
#     if a<b:
#         return True 
#     return False
# print(my_fun7(17925,34**2))




# def my_fun6(a,b):
#     if a>b:
#         return True 
#     return False
# print(my_fun6())




# def my_fun5(a,b):
#     if a>b:
#         return True 
#     return False
# print(my_fun5())


# def my_fun4(a,b,c):
#     if a>b and a<c:
#         return True
#     return False
# print(my_fun4(7,4,8))

# def my_fun3(a,b,c):
#     return a%b*c
# print(my_fun3(7,3,4.8))

# def my_fun2(a,b):
#     return a==b
# print(my_fun2(23+1,22+2))


# def my_fun1(a,b):
#     return a!=b
# print(my_fun1(23+1,22+2))


# def dif(a,b):
#     if a < b:
#         return f'{a} < {b}'
#     elif a==b:
#         return f' {a} == {b}'
#     return f'{a} > {b}'
# a = (12*3)
# b = (13*1)
# print(dif(a, b))




# def my_fun(a,b):
#     return a//b
# print(my_fun(-21,10))



# def god(x):
#     y = 2022
#     c = y - x
#     v = c + 2
#     q = c - 2
#     return f'{v} вам будет через 2 года, {q} вам было 2 года назад'
# print(god(2004))







# def stolet(a):
#     c = (a/100)*100
#     return f' мы прожили {c}% столетия'
# print(stolet(18))



# def sr_arif(a,b,c,d):
#     q = a+b+c+d
#     return q/4
# print(sr_arif(25,75,10,95))


# def my_func2(x,y,z):
#     return x+y*z
# print(my_func2(2.2,2.7,2.3))



# def my_func1(a,b,c,d,e):
#     return (a-e**(b/d)%c)
# print(my_func1(2,5,3.4,3,6))



# def my_funs(a,b):
#     if a < b:
#          return f'{a} < {b}'
#     elif a==b:
#          return f' {a} == {b}'
#     return f'{a} > {b}'
# a = (2**3)
# b = (3**2)
# print(my_funs(a,b))

# def neraz_raz():
#     a = int(input('vvedite luboe chislo ot 0 do 100 >>> '))
#     if a>0 and a<21:
#         print('razresheno')
#     elif a>57 and a<=100:
#         print('razresheno')
#     else:
#         print(' ne zapresheno')
# neraz_raz()


# def chet_nechet(a):
#     if a%2==0:
#         print(f'{a}chetnoe')
#     else:
#         print(f'{a}ne chetnoe')
#         if a**2 >=1000:
#  	        print('bolshe ili ravno 1000')

# chet_nechet(4)




# def funs1():
#     if 0==0:
#         print('Hello')
# funs1()



# def funs2(a,b):
#     if a==b:
#         return a,b
# print(funs2(10//5,10//5))

# def funs3(a: int): 
#     if a > 0:
#         return -a
#     elif a <= 0:
#         return a


# a=int(input('Vvedite chislo:'))
# print(funs3(a))


# def funs(a,b):
#     if a>0 and b>0:
#         return 'polojitelnoe'
#     elif a<0 and b<0:
#         return 'otrisatelnoe'
#     else:
#         return 'polojitelnoe,otrisatelnoe'
# print(funs (10,5))



# def funs(a,b):
#     if a>b:
#         return a+2
#     else:
#         return b+2
# print(funs (10,5))


# def funcc(a):
#     if a<0:
#         return 'otrisatelnoe'
#     elif a>0:
#         return 'polojitelnoe'

# a = int(input(">> "))
# print(funcc(a))


# def funcc1(a):
#     if a>=18:
#         return'sovershennoletnie'
#     elif a<=4:
#         return'rebonok'
#     else:
#         return 'nesovershennoletnie'
# print(funcc1(19))



# def funcc2(a,b):
#     if a//b==0:
#         return True 
#     return False
# print(funcc2(45,6))

# def funcc3(a):
#     if a==2022:
#         return'tekushii god'
#     elif a>=2022:
#         return'god eshe ne nastupil'
#     else:
#         return'god proshel'
# print(funcc3(2012))




# def funcc0(dates_of_birth):
#     dates_of_birth.remove(7)
#     return dates_of_birth

# dates_of_birth = {3,10,11,13,7,31,21,1,10,3,5,6,6}

# print(funcc0(dates_of_birth))


# def fun_ferm(farm_1,farm_2 ):
#     c = farm_2.difference(farm_1)
#     return c 

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# print(fun_ferm(farm_1,farm_2))




# def funcc3(suitcase,t):
#     suitcase.remove(t)
#     return suitcase

# suitcase=['phone','krem ot zagara','maney','key','comp']
# print(funcc3(suitcase, 'key'))



    


# def fun4(a,b):
#     return f'{a} прекрастная профессия {b}'

# dict = {'Katte':'teacher','Roma':'builder','Tima':'student','Milana':'nanny','Bob':'taxi driver'}
# for key, a in dict.items():
#     print(fun4(key,a))






# def countries(south_american_countries):
#     return(set(south_american_countries))
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
#     'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# print(countries(south_american_countries))



# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# def fibonacci(n):
#     n = 1, 1
#     while True:
#         yield a
#         a, b = b, a +b
# def fibonacci(n):
#     cur = 1
#     if n > 2:
#         cur = fibonacci(n-1) + fibonacci(n-2)
#     return cur

# element = input('Введите номер искомого элемента : ')
# element = int(element)
# value = fibonacci(element)
# print(fibonacci(10))


# def fib(n):
#     old = 0
#     cur = 1
#     i = 1
#     yield cur
#     while (i < n):
#         cur, old, i = cur+old, cur, i+1
#         yield cur



# from turtle import *
# import colorsys

# speed(0)
# pensize(3)
# bgcolor('black')
# hue=0.0

# for i in range(300):
#     col = colorsys.hsv_to_rgb(hue,1,1)
#     pencolor(col)
#     hue+=0.005
#     circle(5-i,100)
#     lt(80)
#     circle(5-i,100)
#     rt(100)
# done()
# print("\U0001F618")
