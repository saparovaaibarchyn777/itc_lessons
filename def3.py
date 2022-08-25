# from random import choice
# from os import system
# from string import ascii_letters 

# def my_random(x):
#     for i in range(x):
#         file_name=''
#         while len (file_name)<6:
#             file_name +=choice(ascii_letters)
#         print(f'touch {file_name}.txt')
# my_random(3)



# def polindrom(x):
#     if x!=x[::-1]:
#         return False
#     else:
#         return True 
# print(polindrom('tut')) 


# a = 'hello'
# print(a)
# print(a[::-1])


# a=[56,8,9,45,233,5,4,1,0]
# def sorts(x):
#     x.sort()
#     text =" "
#     for i in x :
#         text += str(i)
#         text += '.'
#     return text
# print(sorts(a))


# def  hello(name,muvi):
#     print(f'Hello: {name}')
#     print(f'Good film: {muvi}')
# hello('Asan','7day')
# hello('Bael','titanik')

# def func1(text):
#     text=f'''<h1>{text}</h1>'''
#     return text
# print(func1('brother'))



# def name(text):
#     for i in text:
#         try:
#             int(i)
#         except:
#             return False
#         return True
# print(name('1234sdfg5'))



# from os import system
# import os
# os.system('ls>files.txt')
# m1=[]
# with open('files.txt','r') as f:
#     m=f.read().split()
#     for i in m:
#         if i.endswith('.txt'):
#             os.system(f'rm -rf {i}')
# a=input('>>')
# def func(l):
#     from os import system
#     os.system('ls > files.txt')
#     l1=[]
#     with open(f'files.txt', 'r') as f:
#         files_names=f.read().split()
#         for i in files_names:
#             if i.endswith(l):
#                 os.system(f'rm -rf {i}')
# func(a)
import os 
os.system('rm -rf sayt.py')