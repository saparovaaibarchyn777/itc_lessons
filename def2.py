# def kvadrat(x,n=2):
#     return x**n
# print(kvadrat(5,3))


# def login(name,age=18):
#     return f'ваше имя ={name},ваш возраст = {age}'
# print(login('Aibarchyn',17))


# def func(*args):
#     for i in  args:
#         if i %2==0:
#             return i 
# print(func(1,2,3,4,5,6,7,8,))

# def func(**kwargs):
#     return kwargs
# print(func(name='aktan',age=17))


# def chet_necheat(x):
#     if x%2==0:
#         return f' {x} chet'
#     else:
#         return f' {x} necheat'
# for i in range(10):
#     print(chet_necheat(i+1))





# def chotnoe(x):
#     if x%2==0:
#         return True
#     return False
# # print(chotnoe(9))




# for i in range(1,20):
#     if chotnoe(i):
#         print(i,'chotnoe')
#     else:
#         print(i,'nechotnoe')


##################  1

# def my_add(a,b):
#     return a+b
# print(my_add(2,6))


# def subtract(z,x):
#     return z-x
# print(subtract(45,5))



# def multiply(a,b):
#     return  a*b
# print(multiply(3,8))


# def divide(z,x):
#     return z//x
# print(divide(24,4))




#################### 2

# def pred_argument(x):
#     y=0
#     for i in x:
#         y +=1
#     return y 
# print(pred_argument('sddd'))


############# 3 
# a = {'name':'Aktan'}
# a2 = {'age':17}
# def dicts(z,x):
#     z.update(x)
#     return z
# print(dicts(a,a2))



##################  4 

# x=input('Что вы хотели  покушать ?>>>   ')
# y = input('Что вы хотели выпить?>>>  ')
# def zakaz(a,b):
#     with open ('menu.txt','w') as file:
#         file.write(a)
#         file.write(b)
# print(x)
# print(y)

    
############ 5



# def new_file(file_name):
#     import os
#     os.system(f'touch {file_name}.txt')

# a = input('Введите имя файла: ')
# new_file(a)



############## 10

# x = int(input('Введите число?>>> \n'))

# def func(n):
#     return f'{n}'*n
# print(func(x))

############ 11

# def info(name,zarplata=5000):
#     return f'Ваше имя ={name},Ваша зарплата={zarplata}'
# print(info('Asek'))


########### 8

# a = []
# for  i in range(2,100):
#     k = 0
#     for j in range(2,i):
#         if i %j==0:
#             k +=1
#     if k ==0:
#         a.append(i)
# print(a)




# a = []
# while True:
#     print(a)
#     z = int(input())
#     if z > 1:
#         for i in range(2, int(z/2)+1):
#             if (z % i) == 0:
#                 print("False")
#                 break
#         else:
#             print("True")
#             a.append(z)
            
#     else:
#         print("False")

############ 7
# def max_f(x):
    
#     def min_f(x):
#         return f'Маленькая функция {x}'
#     print(min_f(x))
     
# max_f('Большая функция')

########### 8 
# def hello():
#     print('hello katte')
#     print('bob ')
#     print ('popo')
# hello()
# print('bobi')
# hello()

# def add(a,b):
#     return a+b
# print(add(35,5))


# def subtract(x,y):
#     return x-y
# print(subtract(67,7))


# def multiply(z,x):
#     return z*x
# print(multiply(2,7))


# def divide(m,n):
#     return m//n
# print(divide(56,9))

# def argument_len(y):
#     x =0
#     for i in y:
#         x+=1
#     return x
# print(argument_len('zsdxcfvgbnm'))


# a={'name':'homa'}
# a1 = {'age':18}
# def update1(v,b):
#     v.update(b)
#     return v
# print(update1(a,a1))


# a = input('Что вы хотелии покушать? \n')
# a1 = input('Что вы хотеди выпить? \n')
# def zakazy(x,y):
#     with open('m.txt','r') as file:
#         file.write(x)
#         file.write(y) 
#     print(a)
#     print(a1)


# def kvadrat(a):
#     return a **2
        
# print(kvadrat(8))

# input('Здрасьте !')
# a = input('Введите ваше имя:')
# b = input('Введите ваш возраст:')
# for i in b:
#     if b <=18 :
#         print('Вы еще ребенок!')
#     elif b >= 18:
#         print('Проходите ')
#     else:
#         print('вы слишком стары')
#         print(i)

# def login(name,age=18):
#     return f'Vash imia ={name},Vash vozrast={age}'
# print(login('Aibarchyn',20))


# def funk(*args):
#     for i in args:
#         if i %2==0:
#             return i
# print(funk(1,2,3,4,5,6,7,8))
####################  

# def summa(a,b):
#     return a+b
# print(summa(23,9))

#################
# def prover_argument(x):
#     y=0
#     for i in x:
#         y +=1
#     return y 
# print(prover_argument('qwertgyhujkl;'))


#################

# def vozvrashenie(a,b):
#     for i in a,b:
#         if i%2==0:
#             print (True) 
#     else:
#             print(False)
#     return a,b
# print(vozvrashenie(3,3))

################# 

# def gl_bukvy(a):
#     b =0
#     for i in a:
#         if i 


###################

# password1=input('pridumaite parol:')
# password2=input('pottverdite parol:')
# def proverka(password1,password2):
#     if password1==password2 and len(password1)>=8:
#         return 'yes'
#     else:
#         return'no'
# print(proverka(password1,password2))

###################
# def vse_funk():
#     print(proverka())
#     print(vozvrashenie())
#     print(summa())
#     print(prover_argument())
# print(vse_funk())

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

