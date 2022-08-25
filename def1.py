# a =[1,2,3,3,4,5,6,7,8,9,0]
# b=[1,2,3,3,4,5,6,9,90,6,7,8,9,0]
# def my_len(maasiv):
#     s = 0 
#     for i in maasiv:
#         s +=1
#         return s

# print(my_len(a))
# print(my_len(b))


# def my_sum(a,b,n):
#     return a +b +n
# a =my_sum(6,7,90)
# print(a)


# print1 = print
 
 
# def print(*a):
#     for i in a:
#         print1(i.upper(), end=' ')




# list=['name','age','1','19']


# list.reverse()
# print(list)


# a = 0
# b = 1
# n = 10 
# i = 0
# while i < n - 2:
#     z = a + b
#     a = b
#     b = z
#     i = i + 1
#     print(z)
# print(b)

##########1list 2 zadanie

# f = [0,1]
# [f.append(f[-2]+f[-1])
# for i in range(8)]
# print(f)


# list=['name','age','1','19']
# def my_reverse(list1):
#     mid = len(list1)//2
#     a=list1[:mid]
#     b =list1[mid:]
#     a.reverse()
#     b.reverse()
#     return a+b
# print(my_reverse)
# a = [1,2,3,4,5,6]
# print(my_reverse(a))


# a = int(input('Введите число:'))
# b = int(input('Введите число:'))
# c = a + b

# print(c)


##############2list 1 zadanie
# def new_file(file_name):
#     a =input('Vvedite nazvanie file:')
#     import os
#     os.system(f'touch {file_name}.nt')

# new_file('world')
# new_file('ketti')
# new_file('get geroup')
# new_file('hello') 
# new_file('rikki') 
################# 2list 1 zadanie


# def gen_number():
#     from  random import choice
#     num = '0444'
#     for x in range(6):
#         num += choice ('145790')
#     return num
# print(gen_number())

# for i in range(1,11):
    
#     print(i+1,f"Ваш номер телефона {gen_number()}")
    

# # def fibonacci(n):
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


##############1list 1zadanie

# list1 = ['age','19','name','1']

# def my_revers(list1):
#     a = list1[:2]
#     b = list1[2:]
#     a.reverse()
#     b.reverse()
#     return a+b
# print(my_revers(list1))