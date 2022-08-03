# a = ['Tima','Rikki']
# b = input('Введите имя:')

# a.append(b)
# print(a)


# a = ['Nina','Tima','Rikki']
# while True:
#      b =input('Введите имя:')
#    #  a.pop
   #  print(a)

   #  a.extend(b)
    # print(len(a))



# a = '     ugyftu')




# a = 'mars ,tilek,argen'
# b =a.find('argen')
# print(b)


# a = ''
# print(type(a))






# a = 'TILEK MARS ARGEN'
# b = 'hjvgfv'
# print(a.lower(),b.upper(),b.title(),b.capitalize())






# from time import sleep 
# import os
# def clear():
#     os.sistem('clear')
# while True:
#     for i in range (1,30):
#         sleep(1)
#         print(i,'RED')
#     for i in range (1,6):
#         sleep(1)
#         clear()
#         print(i,'YELLOW')
#     for i in range (1,30):
#         sleep(1)
#         print(i,'GREEN')




from time import sleep
import os
def clear():
    os.system('clear')
while True:
    for i in range(1,30,1):
        print(f'''


        {i} RED
        
        
        ''')
        sleep(1)
        clear()
    for i in range(1,6,1):
        print(f'''


        {i} YELLOW
        
        
        ''')
        sleep(1)
        clear()
    for i in range(1,30,1):
        print(f'''

        {i} GREEN
        
        
        ''')
        sleep(1)
        clear()
      
