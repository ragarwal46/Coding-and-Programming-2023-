<<<<<<< HEAD
import tkinter
from Student import Student 

parti = 0

addParti(parti)

#TODO: Cannot import functions from other file. 
=======
import Student

# Jeff = Student.Student("jeff", 12, 10, 4.1, 30, 2)
# partiInput = int(input("How many events did Jeff participate in? "))
student = Student.Student(Student.createNewStudent())
>>>>>>> 1e83bec3af55c09f65152de922addf96d5b65710

print(student.name)

student.addParti()
