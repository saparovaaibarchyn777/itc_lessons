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


from re import A


users = {
    '6575687876':{
        'name':'Asan',
        'last_name':'Usonov',
        'b_year':2000,
        'gender':'m',
        'status':False,
        'ID':'JR55666'

    }
}


users = {
    '6579099087':{
        'name':'Uson',
        'last_name':'Asanov',
        'b_year':2002,
        'gender':'m',
        'status':False,
        'ID':'JT566898'

    }
}
inn = input('jjj: ')
name=input('Vvedite name:')
last_name=input('Vvedite last_name:')
b_year=input('Vvedite b_year:')
gender=input(' Vvedite gender:')
status=input('VVedite status:')
id=input('Vvedite id:')





users[inn]={
    'name':name,
    'last_name': last_name,
    'b_year':b_year,
    'gender':gender,
    'status':status,
    'ID':id

}
print(users)