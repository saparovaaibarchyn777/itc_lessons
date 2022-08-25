# class Car:
#     def __init__(self,name:str, number:int, color:str) -> None:
#         self.name = name
#         self.number = number
#         self.color = color 

#     def drive(self):
#         print('machine drive ...')


# class BMW(Car):
#     mator ='W2'

# f10 = BMW('f10',1212,'black')

# f10.drive()
# print(f10.mator)       


# print(dir(f10))





class Person:
    def __init__(self,last_name:str, name:str, ) -> None:
        self.last_name = last_name
        self.name = name 

    def eat(self):
        print('eating ...')

    def sleep(self):
        print('sleeping ...')




class Doktor:
    def __init__(self,last_name:str, name:str, ) -> None:
        self.last_name = last_name
        self.name = name

    
class Nurse(Doktor):
    def injection(self):
        print('injection ...')
    def sleep(self):
        print(f'{self.name} sleeping')

class Electrik:
    def __init__(self,last_name:str, name:str, ) -> None:
        self.last_name = last_name
        self.name = name

    
n = Nurse('Sara','Sarasa')           
n.sleep()
