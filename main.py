import tkinter
from Student import Student

#Parti stands for Participation (in events)

def addParti(currentParti, newParti):
    totalParti = currentParti + newParti
    return totalParti

student1 = Student("bob", 14, 9, 3.9, 22, 4)

print(addParti(student1.parti, 3))



