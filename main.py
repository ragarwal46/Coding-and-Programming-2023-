from doctest import master
from logging import root
import tkinter as tk
from tkinter import ttk
import customtkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox as mb

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)



        # creating a container
        #container = tk.Frame(self) 
        #container.pack(side = "top", fill = "both", expand = True)

        #root = tk.Tk()
        self.geometry("1000x600")
        #root.geometry("1000x600")
        container = tk.Frame(self)
        container.pack(expand = True, fill = "both")

  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, AddStudent, Event):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # ViewStudent, AddStudent, Event respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home)

        
    def show_frame(self, cont):  
        frame = self.frames[cont]  
        frame.tkraise()



class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.actionsLabel = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Actions",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.actionsLabel.grid(row=1, column=0, pady=10, padx=10)

        def open_stuent_table():
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("SELECT * FROM student")
            i=0 
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=20, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        self.showHome = customtkinter.CTkButton(master=self.frame_left,
                                                text="Home",
                                                command=lambda: controller.show_frame(Home))
        self.showHome.grid(row=2, column=0, pady=20, padx=20)


        self.ViewStudentTableButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="View Student Table",
                                                command=open_stuent_table)
        self.ViewStudentTableButton.grid(row=3, column=0, pady=20, padx=20)

        
        self.showAddStudent = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Student",
                                                command=lambda: controller.show_frame(AddStudent))
        self.showAddStudent.grid(row=4, column=0, pady=20, padx=20)
        
        self.showEvent = customtkinter.CTkButton(master=self.frame_left,
                                                text="Event",
                                                command=lambda: controller.show_frame(Event))
        self.showEvent.grid(row=5, column=0, pady=20, padx=20, sticky="n")
      

        
        
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)


        

        self.ViewStudentTableButton = customtkinter.CTkButton(master=self.frame_right,
                                                text="View Student Table",
                                                command=open_stuent_table)
        self.ViewStudentTableButton.place(relx = 0.5, rely = 0.05, anchor = 'center')


    def new_method(self):
        tk.Tk.title = "AAI Student Event Tracker"

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # set default values
    #self.optionmenu_1.set("Dark")
    #self.addstudent.set("Student")

class AddStudent(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
  
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1, 2), weight=1)
        self.frame_right.columnconfigure(3, weight=0)
        
        self.actionsLabel = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Actions",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.actionsLabel.grid(row=1, column=0, pady=10, padx=10)

        def open_stuent_table():
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("SELECT * FROM student")
            i=0 
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=20, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        self.showHome = customtkinter.CTkButton(master=self.frame_left,
                                                text="Home",
                                                command=lambda: controller.show_frame(Home))
        self.showHome.grid(row=2, column=0, pady=20, padx=20)


        self.ViewStudentTableButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="View Student Table",
                                                command=open_stuent_table)
        self.ViewStudentTableButton.grid(row=3, column=0, pady=20, padx=20)

        
        self.showAddStudent = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Student",
                                                command=lambda: controller.show_frame(AddStudent))
        self.showAddStudent.grid(row=4, column=0, pady=20, padx=20)
        
        self.showEvent = customtkinter.CTkButton(master=self.frame_left,
                                                text="Event",
                                                command=lambda: controller.show_frame(Event))
        self.showEvent.grid(row=5, column=0, pady=20, padx=20, sticky="n")


        self.AddStudentLabel = ttk.Label(master=self.frame_right,
                                              text="Add Student",
                                              font=("Roboto Medium", 20),
                                              background='#ebebeb')
        self.AddStudentLabel.place(relx = 0.5, rely = 0.05, anchor='center')

        #Name Fields
        self.name = ttk.Label(master=self.frame_right,
                                                text="Name",
                                                font=("Roboto Medium", 8),
                                                background='#ebebeb')
        self.name.place(relx = 0.08, rely = 0.1)

        self.fname = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'First Name', text_color='black')
        self.fname.place(relx = 0.08, rely = 0.16)
        
        self.lname = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'Last Name', text_color='black')
        self.lname.place(relx = 0.53, rely = 0.16)

        #Age Fields
        self.ageLabel = ttk.Label(master=self.frame_right,
                                              text="Age",
                                              font=("Roboto Medium", 8),
                                              background='#ebebeb')
        self.ageLabel.place(relx = 0.08, rely = 0.26)

        self.age = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'Age (Years)', text_color='black')
        self.age.place(relx = 0.08, rely = 0.32)

        #Grade fields
        self.grade = ttk.Label(master = self.frame_right, text = "Grade",
                                            font=("Roboto Medium", 8),
                                            background='#ebebeb')
        self.grade.place(relx = 0.08, rely = 0.42)
        self.gradelvl = customtkinter.CTkComboBox(master = self.frame_right, values=["9", "10", "11", "12"], state='readonly')
        self.gradelvl.place(relx = 0.08, rely = 0.48)
        self.gradelvl.set('Grade')
        

        #GPA fields
        self.gpalabel = ttk.Label(master=self.frame_right, 
                                            text = 'GPA (Unweighted)',
                                            font=('Roboto Medium', 8),
                                            background='#ebebeb')
        self.gpalabel.place(relx = 0.08, rely = 0.6)

        self.gpa = customtkinter.CTkEntry(master = self.frame_right, width = 100, placeholder_text= 'GPA', text_color='black')
        self.gpa.place(relx = 0.08, rely = 0.66)
        
        
        def add_student_db():
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            try:
                if self.fname.get() == '' or self.lname.get() == '' or self.gradelvl.get() == '' or self.age.get() == '' or self.gpa.get() == '':
                    mb.showwarning("Error", "Please Ensure All Fields are Filled Out")
                elif float(self.gpa.get()) <= 0.0 or float(self.gpa.get()) > 4.0:
                    mb.showwarning("Error", "GPA must be between 0.0 and 4.0")
                else:
                    #executing the sql command
                    my_conn = my_connect.cursor()
                    my_conn.execute("INSERT INTO student (FirstName, LastName, Grade, Age, GPA) Value ('" + self.fname.get() + "', '" + self.lname.get() + "', '" + self.gradelvl.get() + "',  '" + self.age.get() + "', '" + self.gpa.get() + "')")
                    my_connect.commit()
                    mb.showinfo("Success", "Student added")
            except:
                my_connect.rollback()
                mb.showerror("Failed", "Student was not added")


        self.addbutton = customtkinter.CTkButton(master = self.frame_right, text = 'Add', command=add_student_db)
        self.addbutton.place(relx = 0.5, rely = 0.84, anchor = 'center')

class Event(tk.Frame):      
     def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
  
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1, 2), weight=1)
        self.frame_right.columnconfigure(3, weight=0)
        
        self.actionsLabel = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Actions",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.actionsLabel.grid(row=1, column=0, pady=10, padx=10)

        def open_stuent_table():
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("SELECT * FROM student")
            i=0 
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=20, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        self.showHome = customtkinter.CTkButton(master=self.frame_left,
                                                text="Home",
                                                command=lambda: controller.show_frame(Home))
        self.showHome.grid(row=2, column=0, pady=20, padx=20)


        self.ViewStudentTableButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="View Student Table",
                                                command=open_stuent_table)
        self.ViewStudentTableButton.grid(row=3, column=0, pady=20, padx=20)

        
        self.showAddStudent = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Student",
                                                command=lambda: controller.show_frame(AddStudent))
        self.showAddStudent.grid(row=4, column=0, pady=20, padx=20)
        
        self.showEvent = customtkinter.CTkButton(master=self.frame_left,
                                                text="Event",
                                                command=lambda: controller.show_frame(Event))
        self.showEvent.grid(row=5, column=0, pady=20, padx=20, sticky="n")
        def open_event_table():
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("SELECT Name, Type, Points FROM event")
            i=0 
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=30, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        self.ViewStudentTableButton = customtkinter.CTkButton(master=self.frame_right,
                                                text="View Events Table",
                                                command=open_event_table)
        self.ViewStudentTableButton.place(relx = 0.15, rely = 0.05, anchor = 'center')


def on_closing(self, event=0):
        self.destroy()

app = tkinterApp()
app.mainloop()
