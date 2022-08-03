
# from random import choice
# students = ['Каныкей','Бексултан' ,'Айбарчын' ,'Тилек' ,'Арген' ,'Байзак' ,'Актан' ,'Эгида ','Байель' ,'Нурдик ','Искен']
# team1=[]
# team2=[]
# for i in students:
#     while len(team1)!=6:
        
#         name = choice(students)
#         if name not in team1:
#             team1.append(name)
#     while len(team2)!= 5:
#         name = choice(students)
#         if name not in team1 and name not in team2:
#             team2.append(name)
#     print('Komanda1',team1)
    #print('Komanda2',team2)

a = 0 
for i in range(1,1000):
    if i%3==0 or i%5==0:
        a = a+1
        print (a)



    