# try:
#   print(1/0)
# except:
#   print("ZeroDivisionError")

# try:
#     x=int(input())
#     print(x)
# except ValueError as e:
#     print(e)
# except:
#     print("Error")

# try:
#     x=int(input())
#     print(x)
# except:
#     print("Error")
# finally:
#     print("done")


'''We can use else statement in for loop also'''
# for i in range(5):
#     print(i)
# else:
#     print("done")

# for i in range(5):
#     print(i)
#     if i==3:
#         break
# else:
#     print("done")


# try:
#     x=int(input())
#     print(x)
# except:
#     print("error")
# else:
#     print("x is a number")


# with open("file.txt","w") as f:
#     f.write("hello world")

# with open("file.txt","r") as f:
#     print(f.read())

# with open("file.txt","a") as f: #a=append
#      f.write("Keeravani")


# x=int(input())
# if x<0:
#     raise ValueError("number should be positive")


# class dummy():
#     def __init__(self,name):   #init is a constructor and self is the current object
#         self.name=name         #for creating multiple objects we use self
# d=dummy("Keeravani")
# d1=dummy("Hi")
# print(d.name)

# #we get an error because we are trying to print private variable value
# class dummy():
#     def __init__(self,name,age,city):   #init is a constructor and self is the current object
#         self.name=name         #for creating multiple objects we use self
#         self.__age=age    #indicates private variable
#         self._city=city   #indicates protected variable
# d=dummy("Keeravani")       
# print(d.name)
# print(d.age)


# #to avoid error we use setters and getters
# class dummy():
#     def __init__(self,name,age,city):   #init is a constructor and self is the current object
#         self.name=name         #for creating multiple objects we use self
#         self.__age=age
#         self._city=city
#     def getage(self):
#         return self.__age
#     def setage(self,age):
#         self.__age=age
# d=dummy("Keeravani",20,"Vijayawada")
# print(d.getage())


# #infinite loop
# while True:
#     print("hi")


# class Animal():
#     def dummy(self):
#         print("Animal")
#     def sound(self):
#         print("Animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# class Cat(Animal):
#     def sound(self):
#         print("meow")
# d=Dog()
# d1=Cat()
# d2=Animal()
# d.sound()
# d1.sound()
# d.dummy()
# d1.dummy()
# d2.sound()

# #with abstractmethod
# from abc import abstractmethod,ABC
# class BankAccount(ABC):
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         self.balance-=amount
#     def getbalance(self):
#         return self.balance
#     @abstractmethod
#     def interestcal(self):
#         pass

# #without abstractmethod
# class SavingsAcc(BankAccount):
#     def interestcal(self):
#         return 0.03*self.__balance
# S=SavingsAcc(100)