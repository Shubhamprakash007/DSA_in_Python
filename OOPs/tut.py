def my_func(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

x ,y ,z = map(int, (input("enter value of")).split(" "))
name, age, city = input("enter string").split(" ")
my_func(x, y, z, name= name, age=age, city=city)