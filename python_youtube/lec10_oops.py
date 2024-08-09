#creating a class
# class Student:
#     name = "sajid"

# #creating a object
# s1 = Student()
# print(s1)

# class car:
#     color = "white"
#     brand = "wagonR"
# car1 = car()
# print(car1.color)

class Student:
  
#   default constructor
  def __init__(self):
           pass
      
 # parametrized constructor
  def __init__(self,name,marks): # constructor (self == s1 object) in constructor always passes a argument self argument
       self.name=name
       self.marks = marks
       print("adding new student in databse")

    #    methods
  def welcome(self):
      print("welcom method",self.name)

      #Static methods
  @staticmethod
  def hello():
      print("hii yaaar...")

      
#  objects
s1 = Student("sajid",98)
# print(s1.name,s1.marks)
s1.welcome()
s1.hello()

# s2 = Student("malik",89)
# # print(s2.name,s2.marks)