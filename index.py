class Student ():
    name  = 'mifan'
    def __init__ (self , name , age):
        name = name 
        ge = age
  


student = Student('小米',12)

print(student.name)
print(Student.name)
print(student.__dict__)
print(Student.__dict__)
print(Student.__doc__)