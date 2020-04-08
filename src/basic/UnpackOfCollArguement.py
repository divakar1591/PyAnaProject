###EX-1
def myfun(**kwargs):     #kwargs means collection of multiple arguemnt as dictionary
  print(f"All values: {kwargs}")
  # print(f"Pos-0 value: {args[0]}")

myfun(name="Divakar", age=30)

###Ex-2
def myfun2(name, age):
  print(name, age)

dict1 = {"name":"Divakar", "age":30}
myfun2(*dict1) #unpacking
myfun2(**dict1) #unpacking


def both(*args, **kwargs):
  print("=======both function==========")
  print(args)
  print(kwargs)

both(1,3,5,name="Divakar", age=30)

"""
***NOTE: In kwargs, pass only named arguement because it convert it into a dictionary
"""