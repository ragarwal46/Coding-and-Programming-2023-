import Student
from Student import createNewStudent
import tkinter as tk
import tkinter.font as font

#Jeff = Student.Student("jeff", 12, 10, 4.1, 30, 2)
#partiInput = int(input("How many events did Jeff participate in? "))
#print(Jeff.parti + partiInput)



window = tk.Tk()
window.title("Coding and Programing 2023")

generalFont = font.Font(family="sans-serif",)

createStudentbtn = tk.Button(window, text="Add a New Student", border=3, borderwidth=10, width=15, height=2, font=generalFont)

createStudentbtn.pack()

window.mainloop()