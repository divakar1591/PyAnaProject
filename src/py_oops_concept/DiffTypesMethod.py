class Student:

  def instance_method(self):
    print(f"Called instance method of {self}")

  @classmethod
  def class_method(cls): # cls is special arguement which is class itself
    print(f"Called class method of {cls}")

  @staticmethod
  def static_method(): # doesn't get any params as arguments
    print(f"Called static method")




student = Student()
#Instance Method
student.instance_method()
Student.instance_method(student) #If called with Class then need to pass class object
###Class Method
Student.class_method() #If called with Class then no need to pass class object(py pass internally)
###Static Method
Student.static_method()

"""
Instance Method : Used for access class object to change data either by aceess variable or function.
Class Method : Used as a factory method(which called with class not with class object)
Factory Method : For better code organization when not required CLASS or Object in function 
"""