class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):  #return string when object of class converted in string like- print(student)
    return f"Student name : {self.name} and age: {self.age} year old"

  def __str__(self):  #used at debugging time
    return f"Student name : {self.name} and age: {self.age}"


student1 = Student("Rolf", 22)
print(student1)

"""
NOTE: __method_name__ called magic method
"""
