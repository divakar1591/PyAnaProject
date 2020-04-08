class Student:
  def __init__(self):  #Called when class called(similar to constructor of java)
    self.name = "Rolf"
    self.grades = (88, 91, 78, 98, 95)

  def __init__(self, name, grades):  #Called when class called(similar to constructor of java)
    self.name = name
    self.grades = grades

  def average(self):
    return sum(self.grades)/len(self.grades)

########################WITHOUT ARGUMENT
# student = Student() # Creating object of type Student
# print(student.name)
# print(student.average()) #or (Good Practice)
# print(Student.average(student)) # (Bad Practice)

########################WITH ARGUMENT

student1 = Student("Rolf", (88, 91, 78, 98, 95))
student2 = Student("Divakar", (55, 34, 76, 55, 99))

print(student1.name)
print(student1.average())
print(student2.name)
print(student2.average())
