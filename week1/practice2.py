# import keyword
# L = keyword.kwlist
# print("List of keywords: ",L)
# print("number of keywords: ",len(L))

# with open("file_path.txt","r"") as file:
#           file.read()

# a1 = lambda a,b: a+b
# s = a1(10,20)
# print(s)

# a1 = lambda a,b: a*b
# f1 = a1(10,20)
# print(f1)

# a=10

# def fun():
#     global a
#     a = 40
#     print(a)

# fun()
# print(a)

# a = input("Enter a number: ").split(" ")
# print(a)

# print("20"), print("40")

# L= [1,2,3,4,5]
# print(*L)

# print("123","Ahammad","@!@#$",end="--the end---",sep="@@@@@@")

# a1 = "Ahammad"
# a2 = "AI"
# print(f"Hello I am %s i am an %s developer" %(a1,a2))

# print("True" if 10>2 else "False")

# L=[1,2,3,4,5,6]

# L1=[]
# L2=[]

# for i in L:
#     if i not in L1:
#         L1.append(i)
#     else:
#         L2.append(i)

# if L2:
#     print("The duplicate values are: ",L2)
# else:
#     print("There are not duplicate values in the list")

# class A:
#     def __init__(self,a):
#         self.a = a

#     def __add__(self,o):
#         return self.a+o.a
    
# a1 = A(1)
# a2 = A(2)

# a3 = A("Hello")
# a4 = A("AI")

# print(a1+a2)
# print(a3+a4)

# class Employee:
#     def __new__(cls):
#         print("new magic method called")
#         inst = object.__new__(cls)
#         return inst
    
#     def __init__(self):
#         print("__init__ magic method is called")
#         self.name = "Satya"

# emp = Employee()
        

# class Employee:
#     def __init__(self):
#         self.name = "Ahammad"
#         self.salary = 2000

#     def __str__(self):
#         return f"Employee name is {self.name} employee salary is {self.salary}"
    
# emp = Employee()
# print(emp)

# from copy import copy,deepcopy
# a = [100,200,300,400,[500,600,700,[800]]]
# b = deepcopy(a)
# print(id(a))
# print(id(b))
# a[4].append(900)
# print("printing a value: ",a)
# print("printing b value: ",b)

# print("id of a :",id(a))
# print("id of b :",id(b))

# import functools

# L=[1,2,3,4,5]

# fun = functools.reduce(lambda x,y: x+y,L)
# print(fun)

# r = functools.reduce( lambda a,b: a*b,L)
# print(r)

# def fun(x):
#     ovwels = "aeiou"

#     if x in ovwels:
#         return True
#     else:
#         return False
    
# L = ["a","b","e","i","o","m"]

# f = filter(fun,L)
# print(list(f))

# import functools

# L=[1,2,3,4,5]

# s = functools.reduce(lambda a,b: a+b,L)
# print(s)

# L1 = [1,2,3,4,5]

# def func1(a):
#     return a*a
# f1 = map(func1,L1)
# print(list(f1))

# l1=["Ahammad","Satya","AI","Developer"]
# e1 = list(enumerate(l1,start=0))
# print(e1)

# s1 = {1,2,3}
# s1.add(50)
# s1.update([10,30,20])
# print(s1)

# def func(y):
#     x=20
#     return x+y
# print(func(30))

# def fun1(*a):
#     for i in a:
#         print(i)

# fun1(10,20,40,30,50)

# def fun2(**kwargs):
#     for key,value in kwargs.items():
#         print("key is: ",key,"Value is : ",value)

# fun2(name="Ahammad",age="30",city="Guntur")

# def outer():
#     def inner():
#         print("inner function called")
#         return "20"
#     return inner()

# o = outer()
# print(o)


# def inttest(x):
#     x.append(25)
#     print("in function x is: ",x)
#     print("in function x id is: ",id(x))


# x=[15,20]
# inttest(x)
# print("outside function x is: ",x)
# print("outside function x id is: ",id(x))

# def some(a):
#     if a==1:
#         return 1
#     else:
#         return a*some(a-1)
    
# print(sum(5))

# add = lambda x=10: (lambda y: x+y)
# a = add()
# print(a)
# print(a(20))



# def simple1():
#     yield 1
#     yield 2
#     yield 3

# s = simple1()
# for i in s:
#     print(i)

# ite_value = "geeksforgeeks"

# i1 = iter(ite_value)

# print(i1.__next__())
# print(next(i1))


# def fun1(x):
#     def inner(a):
#         return a.upper()
#     return inner

# @fun1
# def outfun(a):
#     return a

# print(outfun("ahammad"))


# def fun1(a):
#     def inner(x):
#         if x%2 ==0:
#             return "Even"
#         else:
#             return "Odd"
        
#     return inner

# @fun1
# def simple(s):
#     return s

# print(simple(50))


# def split(a):
#     def inner1():
#         f = a()
#         return f.split(" ")

#     return inner1

# def upper(y):
#     def inner2():
#         m = y()
#         return m.upper()
#     return inner2

# @split
# @upper
# def main_func():
#     return "This is AI developer"

# print(main_func())


# class ClassName:
#     def __init__(self,a):
#         self.a = a

#     def get_func(self):
#         return self.a
    
# c = ClassName(10)
# print(c.get_func())

# class Mobile:
#     price = 50000
#     def __init__(self):
#         self.model = "iPhone"
    
#     def get_model(self):
#         return self.model
    
#     @classmethod
#     def get_price(cls):
#         return cls.price
    

# m = Mobile()
# print(m.get_model())
# print(m.get_price())
# print(Mobile.price)
# print(m.model)


# class Car:
#     def __init__(self,name):
#         self.__name = name
    
#     def get_name(self):
#         return self.__name

#     def set_name(self,name):
#         self.__name = name

        
    
# c = Car("BMW")
# print(c.get_name())
# # print(c.set_name())

# c.set_name("Audi")
# print(c.get_name())
# # print(c.set_name())



# class Car:
#     fp = "Ali"
#     def __init__(self,name):
#         self.name = name
    
#     @classmethod
#     def class_method(cls):
#         return cls.fp
    
# print(Car.fp)

# class Father:
#     def __init__(self):
#         self.name1= "Ahammad"

#     def get_name(self):
#         print("Father method")
    
# class Son(Father):
#     def __init__(self):
#         super().__init__()
#         self.name = "Satya"

#         print(super().get_name())
#         print(self.name)

#     def get_name1(self):
#         print("son method")

# s = Son()
# s.get_name()
# s.get_name1()



# class Father:
#     def show(self):
#         print("Mastan")

# class Son(Father):
#     def show(self):
#         super().show()
#         # print("Ahammad")

# f = Son()
# f.show()


# from abc import ABC,abstractmethod
# class Polygon(ABC):
#     @abstractmethod
#     def no_of_slides(self):
#         pass

# class Triangle(Polygon):
#     def no_of_slides(self):
#         return 3
    
# t = Triangle()
# print(t.no_of_slides())

# with open("filename",mode= "w") as f:
#           f.write("Hello")


# file = open("file_name","r")
# a =file.read()

# a.close()


# import pickle
# pickle.dump(object,file)

# import pickle

# class Student:
#     def __init__(self,name,roll,address):
#         self.name = name
#         self.roll = roll
#         self.address = address

#     def disp(self):
#         print(f"f'name is {self.name}")

# with open("file_name",mode="r") as f:
#     stu1 = Student("Rahul")
#     pickle.dump(stu1)
#     print("pickling is done!!!")

# with open("file+_name",mode="w") as f1:
#     obj = pickle.load(f)
#     print("unpickling is done!!!")
#     obj.disp()

# try:
#     if 2%2==0:
#         print(True)
#     raise NameError("Hi there")
# except NameError as ne:
#     print(ne)

# else:
#     print("else block executed")

# finally:
#     print("finally block executed")

# import multiprocessing

# def print_cube(num):
#     print("print cube {}".format(num*num*num))

# def print_square(num):
#     print("print square {}".format(num*num))


# mp = multiprocessing.Process(target=print_cube,args=(10,))
# mp1 = multiprocessing.Process(target=print_square,args=(20,))

# mp.start()
# mp1.start()

# mp.join()
# mp1.join()

# print("DOne")


# import threading

# def print_cube(num):
#     print("print cube {}".format(num*num*num))

# def print_square(num):
#     print("print square {}".format(num*num))


# mp = threading.Thread(target=print_cube,args=(10,))
# mp1 = threading.Thread(target=print_square,args=(20,))

# mp.start()
# mp1.start()

# mp.join()
# mp1.join()

# print("DOne")


# from collections import OrderedDict
# L = [1,2,3,4,3,2,1,2,34,4]
# res = collections.Counter(L)
# print(res)

# d1 = {}
# d1["Ahammad"] = 1
# d1["Ali"] = 2
# d1["Shaik"] = 3

# print("d1 is before deleting",d1)
# del d1["Ahammad"]
# print("d1 is after deleting",d1)
# d1["Ahammad"] = 1
# print("d1 is after adding",d1)


# ord1 = OrderedDict()
# ord1["Ahammad"] = 1
# ord1["Ali"] = 2
# ord1["Shaik"] = 3

# print("ord1 is before deleting",ord1)
# del ord1["Ahammad"]
# print("ord1 is after deleting",ord1)
# ord1["Ahammad"] = 1
# print("ord1 is after adding",ord1)

# import re
# s = "Geeks for geeks portal"
# match = re.search(r"portal",s)
# print(match)
# print(match.start())
# print(match.end())



# Author.objects.create(name="Ada",email="ali@gmail.com")
# Book.objects.get(id=1)
# Book.objects.filter(id__gt = 2)
# Book.objects.exclude(author__name="Ahammad")

# Book.objects.filter(pk=1).update(name="Ali")

# Book.objects.filter(published__year__lt=2000).delete()

# from django.db.models import Count,Avg,F,Q


# from django.db.models import Count,Avg,Q,F

# Author.objects.annotate(num__books = Count("books"))
# Book.objects.aggregate(avg=Avg("pages"))
# Book.objects.update(pages=F("pages") +1)
# Book.objects.filter(Q(pages__gt=300) | Q(title__startswith="D"))


# author.objects.create(name="",book="")
# author.objects.filter(name__startswith="ah")
# author.objects.get(id=1)
# author.objects.exclude(name__startswith="Ah")

# Book.objects.filter(id=1).update(name="Sai")

# Book.objects.filter(publishdate__year__lt=2000).delete()

# from django.db.models import Count,F,Q
# Author.objects.annotate(num__books = Count("books"))
# Book.objects.aggregate(avg=Avg("pages"))
# Book.objects.update(pages=F("pages")+1)
# Book.objects.filter(Q(pages__lt=200) | Q(title__starswith="hero"))


# from djanmgo.db.models import Count,Q,F
# Book.objects.annotate(num__books = Count("Books"))
# Book.objects.update(pages= F("count")+1)
# Book.objects.filter(Q(name__startswith="Ahammad") | Q(title__endswith="Hero"))

# Book.objects.select_related("name")
# Book.objects.prefatch_related("city_set").get(name="abgdhsgf")

# python manage.py makemigrations
# python manage.py migrate


# python amnage.py sjowmigrations
# python manage.py sqlmigrate blogm 0001

# python manage.py migrate blog 0001

# pythgon manage.py squashmigrations blog 0001 0100