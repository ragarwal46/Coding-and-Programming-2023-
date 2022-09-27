import Student

# Jeff = Student.Student("jeff", 12, 10, 4.1, 30, 2)
# partiInput = int(input("How many events did Jeff participate in? "))
student = Student.Student(Student.createNewStudent())

print(student.name)

student.addParti()
