# def my_func(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(key, value)

# x ,y ,z = map(int, (input("enter value of")).split(" "))
# name, age, city = input("enter string").split(" ")
# my_func(x, y, z, name= name, age=age, city=city)

# def my_decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper


# # say_hello = my_decorator(say_hello)
# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# def my_decorator1(func):
#     def wrapper():
#         print("Before my_decorator1 is called.")
#         func()
#         print("After my_decorator1 is called.")
#     return wrapper

# def my_decorator2(func):
#     def wrapper():
#         print("Before my_decorator2 is called.")
#         func()
#         print("After my_decorator2 is called.")
#     return wrapper

# say_hello = my_decorator1(my_decorator2(say_hello))
# @my_decorator1
# @my_decorator2
# def say_hello():
#     print("Hello!")

# say_hello()
# s = str()
# import random 
# import time 

# names = ['Sunny','Bunny','Chinny','Vinny'] 
# subjects = ['Python','Java','Blockchain'] 
 
# #list
# def people_list(num_people): 
#     results = [] 
#     for i in range(num_people): 
#       person = { 
#                 'id':i, 
#                  'name': random.choice(names), 
#                  'subject':random.choice(subjects) 
#            } 
#     results.append(person) 
#     return results 
 
# #generator
# def people_generator(num_people): 
#     for i in range(num_people): 
#         person = { 
#             'id':i, 
#             'name': random.choice(names), 
#             'major':random.choice(subjects)
#         }
#         yield person 

# t1 = time.perf_counter()
# people = people_list(10000000)
# t2 = time.perf_counter()

# t1 = time.perf_counter() 
# people = people_generator(10000000) 
# t2 = time.perf_counter() 

# print('Took {}'.format(t2-t1))

class Shubham:
    '''this is a docstirng to show how docstirng works in 
    python using class to larn class '''
    name = "shubham"

print(Shubham.__doc__)
 