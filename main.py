from doctest import master
from logging import root
import tkinter as tk
from tkinter import ttk
import customtkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"



class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)


        self.geometry("1000x600")
        self.title("Alliance Academy For Innovation Student Event Tracker")
        container = tk.Frame(self)
        container.pack(expand = True, fill = "both")

  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, AddStudent, Event, Results):
  
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
                                                text="Assign Event",
                                                command=lambda: controller.show_frame(Event))
        self.showEvent.grid(row=5, column=0, pady=20, padx=20, sticky="n")

        self.showResults = customtkinter.CTkButton(master=self.frame_left,
                                                text="Results",
                                                command=lambda: controller.show_frame(Results))
        self.showResults.grid(row=6, column=0, pady=20, padx=20)
      

        
        
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
        self.Label = ttk.Label(master=self.frame_right,
                                              text="Welcome to the Alliance Academy Student Event Tracker",
                                              font=("Roboto Medium", 20),
                                              background='#ebebeb')
        self.Label.place(relx = 0.5, rely = 0.05, anchor='center')
        
        self.image1 = ImageTk.PhotoImage(Image.open("pic1.jpg"))
        self.image2 = ImageTk.PhotoImage(Image.open("pic2.jpg"))
        self.image3 = ImageTk.PhotoImage(Image.open("pic3.jpg"))
        self.image4 = ImageTk.PhotoImage(Image.open("pic4.jpg"))
        
        self.image_label = Label(master=self.frame_right, image=self.image1)
        self.image_label.place(relx = 0.5, rely = 0.525, anchor = 'center')
        self.current_image = 0
        self.button1 = customtkinter.CTkButton(master=self.frame_right, text=">", text_font=('arial', 15, 'bold'), command=self.on_next, width=25)
        self.button1.place(relx = 0.91, rely = 0.525, anchor = 'center')
        self.button2 = customtkinter.CTkButton(master=self.frame_right, text="<", text_font=('arial', 15, 'bold'), command=self.on_back, width=25)
        self.button2.place(relx = 0.09, rely = 0.525, anchor = 'center')
    
    def on_next(self):
        if self.current_image == 0:
            self.image_label.config(image=self.image2)
            self.current_image += 1
        elif self.current_image == 1:
            self.image_label.config(image=self.image3)
            self.current_image += 1
        elif self.current_image == 2:
            self.image_label.config(image=self.image4)
            self.current_image += 1
        else:
            self.image_label.config(image=self.image1)
            self.current_image = 0
    def on_back(self):
        if self.current_image == 0:
            self.image_label.config(image=self.image4)
            self.current_image = 3 
        elif self.current_image == 1: 
            self.image_label.config(image=self.image1)
            self.current_image -= 1 
        elif self.current_image == 2: 
            self.image_label.config(image=self.image2)
            self.current_image -= 1
        else:
            self.image_label.config(image=self.image3)
            self.current_image -= 1
        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

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
                                                text="Assign Event",
                                                command=lambda: controller.show_frame(Event))
        self.showEvent.grid(row=5, column=0, pady=20, padx=20, sticky="n")


        self.AddStudentLabel = ttk.Label(master=self.frame_right,
                                              text="Add Student",
                                              font=("Roboto Medium", 20),
                                              background='#ebebeb')
        self.AddStudentLabel.place(relx = 0.5, rely = 0.05, anchor='center')

        self.showResults = customtkinter.CTkButton(master=self.frame_left,
                                                text="Results",
                                                command=lambda: controller.show_frame(Results))
        self.showResults.grid(row=6, column=0, pady=20, padx=20)

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
                                                text="Assign Event",
                                                command=lambda: controller.show_frame(Event))
        self.showEvent.grid(row=5, column=0, pady=20, padx=20, sticky="n")

        self.AssignEventLabel = ttk.Label(master=self.frame_right,
                                              text="Assign an Event",
                                              font=("Roboto Medium", 20),
                                              background='#ebebeb')
        self.AssignEventLabel.place(relx = 0.5, rely = 0.05, anchor='center')


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
            my_conn.execute("SELECT * FROM event")
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
        self.ViewStudentTableButton.place(relx = 0.08, rely = 0.03)

        self.showResults = customtkinter.CTkButton(master=self.frame_left,
                                                text="Results",
                                                command=lambda: controller.show_frame(Results))
        self.showResults.grid(row=6, column=0, pady=20, padx=20)
        
        #Student ID Fields
        self.StudentIDLabel = ttk.Label(master=self.frame_right,
                                                text="Student ID",
                                                font=("Roboto Medium", 8),
                                                background='#ebebeb')
        self.StudentIDLabel.place(relx = 0.08, rely = 0.13)

        self.StudentID = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'Student ID', text_color='black')
        self.StudentID.place(relx = 0.08, rely = 0.19)


        #Events fields
        self.EventsLabel = ttk.Label(master = self.frame_right, text = "Events",
                                            font=("Roboto Medium", 8),
                                            background='#ebebeb')
        self.EventsLabel.place(relx = 0.08, rely = 0.26)
        self.EventsDropdown = customtkinter.CTkComboBox(master = self.frame_right, values=["Basketball", "Football", "Baseball", "Golf", "Soccer", "Band Competition", "Robotics", "Technology Competition", "Painting Competition", "Academic Bowl"], state='readonly')
        self.EventsDropdown.place(relx = 0.08, rely = 0.32)
        self.EventsDropdown.set('Select an Event')




        def assign_event_db():
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            try:
                if self.StudentID.get() == "" or self.EventsDropdown.get() == "":
                    mb.showwarning("Error", "Please Ensure All Fields are Filled Out")
                else:
                    
                    EventIDSelected = 0
                    if(self.EventsDropdown.get() == "Basketball"):
                        EventIDSelected = 1
                    elif(self.EventsDropdown.get() == "Football"):
                        EventIDSelected = 2
                    elif(self.EventsDropdown.get() == "Baseball"):
                        EventIDSelected = 3
                    elif(self.EventsDropdown.get() == "Golf"):
                        EventIDSelected = 4
                    elif(self.EventsDropdown.get() == "Soccer"):
                        EventIDSelected = 5
                    elif(self.EventsDropdown.get() == "Band Competition"):
                        EventIDSelected = 6
                    elif(self.EventsDropdown.get() == "Robotics"):
                        EventIDSelected = 7
                    elif(self.EventsDropdown.get() == "Technology Competition"):
                        EventIDSelected = 8
                    elif(self.EventsDropdown.get() == "Painting Competition"):
                        EventIDSelected = 9
                    elif(self.EventsDropdown.get() == "Academic Bowl"):
                        EventIDSelected = 10


                    #executing the sql command
                    my_conn = my_connect.cursor()
                    my_conn.execute("INSERT INTO EventTracker (StudentID, EventID) Value ('" + self.StudentID.get() + "', '" + str(EventIDSelected) + "')")
                    my_connect.commit()
                    mb.showinfo("Success", "Event Assigned")
            except:
                my_connect.rollback()
                mb.showerror("Failed", "Event was not assigned")


        self.assignEventbutton = customtkinter.CTkButton(master = self.frame_right, text = 'Assign', command=assign_event_db)
        self.assignEventbutton.place(relx = 0.08, rely = 0.45)

class Results(tk.Frame):
     
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
                                                text="Assign Event",
                                                command=lambda: controller.show_frame(Event))
        self.showEvent.grid(row=5, column=0, pady=20, padx=20, sticky="n")


        self.showResults = customtkinter.CTkButton(master=self.frame_left,
                                                text="Results",
                                                command=lambda: controller.show_frame(Results))
        self.showResults.grid(row=6, column=0, pady=20, padx=20)


        self.ViewResultsLabel = ttk.Label(master=self.frame_right,
                                              text="View Results",
                                              font=("Roboto Medium", 20),
                                              background='#ebebeb')
        self.ViewResultsLabel.place(relx = 0.5, rely = 0.05, anchor='center')

        
        def showTopWinner():
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            try:
                my_conn = my_connect.cursor()
                topWinner = my_conn.execute("select s.FirstName, s.LastName, count(et.StudentID) as TotalPoints from eventtracker et inner join student s on et.StudentID=s.StudentID group by et.StudentID order by count(et.StudentID) desc limit 1")
                
                i=0 
                for student in my_conn:
                    mb.showinfo("Top Winner", "Congratulations to " + student[0] + " " + student[1] + " who received " + str(student[2])  + " points")
                    i=i+1
            except:
                my_connect.rollback()
                mb.showerror("Failed", "Top winner could not be found")


        self.topWinnerButton = customtkinter.CTkButton(master = self.frame_right, text = 'Top Winner', command=showTopWinner)
        self.topWinnerButton.place(relx = 0.1, rely = 0.13)

        self.randomWinnerButton = customtkinter.CTkButton(master = self.frame_right, text = 'Random Winner')
        self.randomWinnerButton.place(relx = 0.4, rely = 0.13)

        def showQuarterlyReport():
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            my_conn = my_connect.cursor()
            ####### end of connection ####
            my_conn.execute("select s.FirstName, s.LastName, s.Grade, s.Age, s.GPA, count(et.StudentID) as TotalPoints from eventtracker et inner join student s on et.StudentID=s.StudentID group by et.StudentID order by s.Grade, s.FirstName, s.LastName")
            i=0 
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=15, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        self.reportButton = customtkinter.CTkButton(master = self.frame_right, text = 'Generate Quarterly Report', command=showQuarterlyReport)
        self.reportButton.place(relx = 0.7, rely = 0.13)


def on_closing(self, event=0):
        self.destroy()

app = tkinterApp()
app.mainloop()
