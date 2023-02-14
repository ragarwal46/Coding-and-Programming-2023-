#Here are all of our imported libraries which we will use throughout the program

from doctest import master
from logging import root
import tkinter as tk
from tkinter import ttk
import customtkinter
from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
from PIL import Image, ImageTk

customtkinter.set_default_color_theme("blue")  # This sets the default theme of the app
customtkinter.set_appearance_mode("light")


def showSidebar(self, parent, controller): # The purpose of this function is to have the sidebar displayed and be easily changeable
    # ============ frame_left ============

        # Configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10) 
        self.frame_left.grid_rowconfigure(5, weight=1) 
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        # AAI School Logo
        self.logo = ImageTk.PhotoImage(Image.open("Pictures/logo.png"))
        self.logo_label = Label(master=self.frame_left, image=self.logo, bg = '#d1d5d8')
        self.logo_label.grid(row = 0, column = 0, pady = 10, padx = 10)
        
        self.actionsLabel = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Actions",
                                              text_font=("Roboto Medium", -16))
        self.actionsLabel.grid(row=1, column=0, pady=10, padx=10)

        def open_stuent_table():
            # Creating a new window (for the table) and providing credentials to the database
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            # Connecting to the database and writing a query
            my_conn = my_connect.cursor()
            my_conn.execute("SELECT * FROM student ORDER BY Grade")

            # Labeling the columns for the table
            columnHeader1=Label(my_w,width=10,text='Student ID',borderwidth=0, anchor='w')
            columnHeader1.grid(row=0,column=0, sticky='w')
            columnHeader2=Label(my_w,width=10,text='First Name',borderwidth=0, anchor='w')
            columnHeader2.grid(row=0,column=1, sticky='w')
            columnHeader3=Label(my_w,width=10,text='Last Name',borderwidth=0, anchor='w')
            columnHeader3.grid(row=0,column=2, sticky='w')
            columnHeader4=Label(my_w,width=10,text='Grade',borderwidth=0, anchor='w')
            columnHeader4.grid(row=0,column=3, sticky='w')
            columnHeader5=Label(my_w,width=10,text='Age',borderwidth=0, anchor='w')
            columnHeader5.grid(row=0,column=4, sticky='w')
            columnHeader6=Label(my_w,width=10,text='GPA',borderwidth=0, anchor='w')
            columnHeader6.grid(row=0,column=5, sticky='w')

            i=1
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=20, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        # These are all buttons located on the sidebar
        self.showHomeButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="Home",
                                                command=lambda: controller.show_frame(Home))
        self.showHomeButton.grid(row=2, column=0, pady=20, padx=20, sticky="n")


        self.viewStudentTableButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="View Student Table",
                                                command=open_stuent_table)
        self.viewStudentTableButton.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        
        self.showAddStudentButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="Add Student",
                                                command=lambda: controller.show_frame(AddStudent))
        self.showAddStudentButton.grid(row=4, column=0, pady=20, padx=20, sticky="n")
        
        self.showEventButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="Assign Event",
                                                command=lambda: controller.show_frame(logInView)) #should be Event but for now I am trying to test the log in page
        self.showEventButton.grid(row=5, column=0, pady=20, padx=20, sticky="ne")

        self.showResultsButton = customtkinter.CTkButton(master=self.frame_left,
                                                text="Results",
                                                command=lambda: controller.show_frame(studentView)) #show_frame(Results) is the actual command. On the side for testing sutdent view page
        self.showResultsButton.grid(row=6, column=0, pady=20, padx=20, sticky="n")




class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Setting the defaults for the window (such as window title and size)
        self.geometry("1000x625")
        self.title("Alliance Academy For Innovation Student Event Tracker")
        container = tk.Frame(self)
        container.pack(expand = True, fill = "both")

  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, AddStudent, Event, Results, studentView, logInView):
  
            frame = F(container, self)
  
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home)

        
    def show_frame(self, cont):  
        frame = self.frames[cont]  
        frame.tkraise()


class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        showSidebar(self, parent, controller)


        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.titleLabel = ttk.Label(master=self.frame_right,
                                              text="Welcome to the Alliance Academy Student Event Tracker",
                                              font=("Roboto Medium", 20),
                                              background='#d1d5d8')
        self.titleLabel.place(relx = 0.5, rely = 0.05, anchor='center')
        

        # Creation of the Gallery located in the middle of the page
        self.galleryImage1 = ImageTk.PhotoImage(Image.open("Pictures/pic1.jpg"))
        self.galleryImage2 = ImageTk.PhotoImage(Image.open("Pictures/pic2.jpg"))
        self.galleryImage3 = ImageTk.PhotoImage(Image.open("Pictures/pic3.jpg"))
        self.galleryImage4 = ImageTk.PhotoImage(Image.open("Pictures/pic4.jpg"))
        self.galleryImage5 = ImageTk.PhotoImage(Image.open("Pictures/pic5.png"))
        self.galleryImage6 = ImageTk.PhotoImage(Image.open("Pictures/pic6.png"))
        self.galleryImage7 = ImageTk.PhotoImage(Image.open("Pictures/pic7.png"))
 
        self.image_label = Label(master=self.frame_right, image=self.galleryImage1)
        self.image_label.place(relx = 0.5, rely = 0.43, anchor = 'center')
        self.current_image = 1
        self.nextButton = customtkinter.CTkButton(master=self.frame_right, text=">", text_font=('arial', 15, 'bold'), command=self.on_next, width=25)
        self.nextButton.place(relx = 0.91, rely = 0.43, anchor = 'center')
        self.previousButon = customtkinter.CTkButton(master=self.frame_right, text="<", text_font=('arial', 15, 'bold'), command=self.on_back, width=25)
        self.previousButon.place(relx = 0.09, rely = 0.43, anchor = 'center')

        self.helpTitleLabel = ttk.Label(master=self.frame_right,
                                                text="Help",
                                                font=("Roboto Medium", 15),
                                                background='#d1d5d8')
        self.helpTitleLabel.place(relx = 0.1, rely = 0.77)

        self.helpLabel1 = ttk.Label(master=self.frame_right,
                                                text="View Student Table: This button launches a window that shows a list of all of the students with their associated information.",
                                                font=("Roboto Medium", 10),
                                                background='#d1d5d8')
        self.helpLabel1.place(relx = 0.1, rely = 0.82)

        self.helpLabel2 = ttk.Label(master=self.frame_right,
                                                text="Add Student: Shows a form that allows you to enroll a new student into Alliance Academy.",
                                                font=("Roboto Medium", 10),
                                                background='#d1d5d8')
        self.helpLabel2.place(relx = 0.1, rely = 0.86)

        self.helpLabel3 = ttk.Label(master=self.frame_right,
                                                text="Assign Events: Launches a page which shows a form that allows you to add events to any particular student.",
                                                font=("Roboto Medium", 10),
                                                background='#d1d5d8')
        self.helpLabel3.place(relx = 0.1, rely = 0.90)

        self.helpLabel4 = ttk.Label(master=self.frame_right,
                                                text="Results: Shows a page with multiple buttons allowing you to view winners and reports.",
                                                font=("Roboto Medium", 10),
                                                background='#d1d5d8')
        self.helpLabel4.place(relx = 0.1, rely = 0.94)
    
    def on_next(self):
        if self.current_image == 1:
            self.image_label.config(image=self.galleryImage2)
            self.current_image +=1 
        elif self.current_image == 2:
            self.image_label.config(image=self.galleryImage3)
            self.current_image +=1 
        elif self.current_image == 3:
            self.image_label.config(image=self.galleryImage4)
            self.current_image +=1    
        elif self.current_image == 4:
            self.image_label.config(image=self.galleryImage5)
            self.current_image +=1
        elif self.current_image == 5:
            self.image_label.config(image=self.galleryImage6)
            self.current_image +=1
        elif self.current_image == 6:
            self.image_label.config(image=self.galleryImage7)
            self.current_image +=1
        else:
            self.current_image = 1
            self.image_label.config(image=self.galleryImage1)
    def on_back(self):
        if self.current_image == 0:
            self.image_label.config(image=self.galleryImage4)
            self.current_image = 7 
        elif self.current_image == 1: 
            self.image_label.config(image=self.galleryImage1)
            self.current_image -= 1 
        elif self.current_image == 2: 
            self.image_label.config(image=self.galleryImage2)
            self.current_image -= 1
        elif self.current_image == 3: 
            self.image_label.config(image=self.galleryImage3)
            self.current_image -= 1
        elif self.current_image == 4: 
            self.image_label.config(image=self.galleryImage4)
            self.current_image -= 1
        elif self.current_image == 5: 
            self.image_label.config(image=self.galleryImage5)
            self.current_image -= 1
        elif self.current_image == 6: 
            self.image_label.config(image=self.galleryImage6)
            self.current_image -= 1
        elif self.current_image == 7: 
            self.image_label.config(image=self.galleryImage7)
            self.current_image -= 1
        else:
            self.image_label.config(image=self.galleryImage7)
            self.current_image -= 1

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

class AddStudent(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
  
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        showSidebar(self, parent, controller)
        
        self.titleLabel = ttk.Label(master=self.frame_right,
                                              text="Add Student",
                                              font=("Roboto Medium", 20),
                                              background='#d1d5d8')
        self.titleLabel.place(relx = 0.5, rely = 0.07, anchor='center')

        # Name Fields
        self.nameLabel = ttk.Label(master=self.frame_right,
                                                text="Name",
                                                font=("Roboto Medium", 8),
                                                background='#d1d5d8')
        self.nameLabel.place(relx = 0.08, rely = 0.1)

        self.fname = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'First Name', text_color='black')
        self.fname.place(relx = 0.08, rely = 0.16)
        
        self.lname = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'Last Name', text_color='black')
        self.lname.place(relx = 0.53, rely = 0.16)

        # Age Fields
        self.ageLabel = ttk.Label(master=self.frame_right,
                                              text="Age",
                                              font=("Roboto Medium", 8),
                                              background='#d1d5d8')
        self.ageLabel.place(relx = 0.08, rely = 0.26)

        self.age = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'Age (Years)', text_color='black')
        self.age.place(relx = 0.08, rely = 0.32)

        # Grade fields
        self.grade = ttk.Label(master = self.frame_right, text = "Grade",
                                            font=("Roboto Medium", 8),
                                            background='#d1d5d8')
        self.grade.place(relx = 0.08, rely = 0.42)

        gradeNum = tk.StringVar()
        
        self.gradeRadio9 = ttk.Radiobutton(master = self.frame_right, text="9th Grade", value='9', variable=gradeNum)
        self.gradeRadio9.place(relx = 0.08, rely = 0.48)

        self.gradeRadio10 = ttk.Radiobutton(master = self.frame_right, text="10th Grade", value='10', variable=gradeNum)
        self.gradeRadio10.place(relx = 0.23, rely = 0.48)

        self.gradeRadio11 = ttk.Radiobutton(master = self.frame_right, text="11th Grade", value='11', variable=gradeNum)
        self.gradeRadio11.place(relx = 0.08, rely = 0.55)

        self.gradeRadio12 = ttk.Radiobutton(master = self.frame_right, text="12th Grade", value='12', variable=gradeNum)
        self.gradeRadio12.place(relx = 0.23, rely = 0.55)
        

        # GPA fields
        self.gpalabel = ttk.Label(master=self.frame_right, 
                                            text = 'GPA (Unweighted)',
                                            font=('Roboto Medium', 8),
                                            background='#d1d5d8')
        self.gpalabel.place(relx = 0.08, rely = 0.63)

        self.gpa = customtkinter.CTkEntry(master = self.frame_right, width = 100, placeholder_text= 'GPA', text_color='black')
        self.gpa.place(relx = 0.08, rely = 0.69)
        
        
        def add_student_db(): # This function takes all the data from the inputs and then adds it to the database
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            try:
                if self.fname.get() == '' or self.lname.get() == '' or gradeNum.get() == '' or self.age.get() == '' or self.gpa.get() == '':
                    mb.showwarning("Error", "Please Ensure All Fields are Filled Out")
                elif float(self.gpa.get()) <= 0.0 or float(self.gpa.get()) > 4.0:
                    mb.showwarning("Error", "GPA must be between 0.0 and 4.0")
                else:
                    #executing the sql command
                    my_conn = my_connect.cursor()
                    my_conn.execute("INSERT INTO student (FirstName, LastName, Grade, Age, GPA) Value ('" + self.fname.get() + "', '" + self.lname.get() + "', '" + 
                                    gradeNum.get() + "',  '" + self.age.get() + "', '" + self.gpa.get() + "')")
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
  
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        showSidebar(self, parent, controller)


        self.Label = ttk.Label(master=self.frame_right,
                                              text="Assign an Event",
                                              font=("Roboto Medium", 20),
                                              background='#d1d5d8')
        self.Label.place(relx = 0.5, rely = 0.07, anchor='center')

        def open_event_table(): # This function opens a static table that displays a list of all of the events (Sporting & Non-Sporting)
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

            column1=Label(my_w,width=10,text='Event ID',borderwidth=0, anchor='w')
            column1.grid(row=0,column=0, sticky='w')
            column2=Label(my_w,width=10,text='Event Name',borderwidth=0, anchor='w')
            column2.grid(row=0,column=1, sticky='w')
            column3=Label(my_w,width=10,text='Event Type',borderwidth=0, anchor='w')
            column3.grid(row=0,column=2, sticky='w')
            column4=Label(my_w,width=10,text='Event Points',borderwidth=0, anchor='w')
            column4.grid(row=0,column=3, sticky='w')

            i=1 
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=25, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        self.ViewStudentTableButton = customtkinter.CTkButton(master=self.frame_right,
                                                text="View Events Table",
                                                command=open_event_table)
        self.ViewStudentTableButton.place(relx = 0.08, rely = 0.13)
        
        # Student ID Fields
        self.StudentIDLabel = ttk.Label(master=self.frame_right,
                                                text="Student ID",
                                                font=("Roboto Medium", 8),
                                                background='#d1d5d8')
        self.StudentIDLabel.place(relx = 0.08, rely = 0.23)

        self.StudentID = customtkinter.CTkEntry(master=self.frame_right, width = 200, placeholder_text= 'Student ID', text_color='black')
        self.StudentID.place(relx = 0.08, rely = 0.29)


        # Events fields
        self.EventsLabel = ttk.Label(master = self.frame_right, text = "Events",
                                            font=("Roboto Medium", 8),
                                            background='#d1d5d8')
        self.EventsLabel.place(relx = 0.08, rely = 0.36)

        self.EventsDropdown = customtkinter.CTkComboBox(master = self.frame_right, values=["Basketball", "Football", "Baseball", "Golf", "Soccer", "Band Competition", "Robotics", "Technology Competition", "Needs Tutoring", "Tutor Peers"], state='readonly')
        self.EventsDropdown.place(relx = 0.08, rely = 0.42)
        self.EventsDropdown.set('Select an Event')

        def assign_event_db(): # This function adds the information regarding events to a specific student
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
                    elif(self.EventsDropdown.get() == "Needs Tutoring"):
                        EventIDSelected = 9
                    elif(self.EventsDropdown.get() == "Tutor Peers"):
                        EventIDSelected = 10


                    #executing the sql command
                    my_conn = my_connect.cursor()
                    my_conn.execute("INSERT INTO EventTracker (StudentID, EventID) Value ('" + self.StudentID.get() + "', '" + str(EventIDSelected) + "')")
                    my_connect.commit()
                    mb.showinfo("Success", "Event Assigned")
            except:
                my_connect.rollback()
                mb.showerror("Failed", "Event was not assigned.\nPlease ensure the Student ID is correct.")


        self.assignEventbutton = customtkinter.CTkButton(master = self.frame_right, text = 'Assign', command=assign_event_db)
        self.assignEventbutton.place(relx = 0.08, rely = 0.55)
    
        # The following two functions analyze all the student's GPA(s) and reccomends them to either get tutored by a peer, or give tutoring to another
        def studentsWhoNeedTutoring():
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            try:
                my_conn = my_connect.cursor()
                my_conn.execute("SELECT FirstName, LastName, GPA FROM student WHERE GPA < (SELECT avg(GPA) from Student) ORDER BY GPA Desc")
                

                column1=Label(my_w,width=10,text='First Name',borderwidth=0, anchor='w')
                column1.grid(row=0,column=0, sticky='w')
                column2=Label(my_w,width=10,text='Last Name',borderwidth=0, anchor='w')
                column2.grid(row=0,column=1, sticky='w')
                column3=Label(my_w,width=10,text='GPA',borderwidth=0, anchor='w')
                column3.grid(row=0,column=2, sticky='w')

                i=1 
                for student in my_conn: 
                    for j in range(len(student)):
                        e = Entry(my_w, width=25, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student[j])
                    i=i+1

            except:
                my_connect.rollback()
                mb.showerror("Failed", "Reccomendations could not be found")

        def studentsAvaliableToTutor():
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            try:
                my_conn = my_connect.cursor()
                my_conn.execute("SELECT FirstName, LastName, GPA FROM student WHERE GPA > (SELECT avg(GPA) from Student) ORDER BY GPA Desc")
                

                column1=Label(my_w,width=10,text='First Name',borderwidth=0, anchor='w')
                column1.grid(row=0,column=0, sticky='w')
                column2=Label(my_w,width=10,text='Last Name',borderwidth=0, anchor='w')
                column2.grid(row=0,column=1, sticky='w')
                column3=Label(my_w,width=10,text='GPA',borderwidth=0, anchor='w')
                column3.grid(row=0,column=2, sticky='w')

                i=1 
                for student in my_conn: 
                    for j in range(len(student)):
                        e = Entry(my_w, width=25, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student[j])
                    i=i+1

            except:
                my_connect.rollback()
                mb.showerror("Failed", "Reccomendations could not be found")
        
        self.recomendationLabel = ttk.Label(master = self.frame_right, text = "Recomended Events: ",
                                            font=("Roboto Medium", 8),
                                            background='#d1d5d8')
        self.recomendationLabel.place(relx = 0.67, rely = 0.13)

        self.needsTutoringButton = customtkinter.CTkButton(master = self.frame_right, text = 'Students Who Need Tutoring', command=studentsWhoNeedTutoring)
        self.needsTutoringButton.place(relx = 0.67, rely = 0.19)

        self.canTutorButton = customtkinter.CTkButton(master = self.frame_right, text = 'Students Available To Tutor', command=studentsAvaliableToTutor)
        self.canTutorButton.place(relx = 0.67, rely = 0.32)



class Results(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
  
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        showSidebar(self, parent, controller)

        self.ViewResultsLabel = ttk.Label(master=self.frame_right,
                                              text="View Results",
                                              font=("Roboto Medium", 20),
                                              background='#d1d5d8')
        self.ViewResultsLabel.place(relx = 0.5, rely = 0.07, anchor='center')

        
        def showTopWinner(): # This funciton finds the student with the highest number of points and displays them in an alert box
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
                    mb.showinfo("Top Winner", "Congratulations to our winner " + student[0] + " " + student[1] + " who received " + str(student[2])  + " points.\n\n" + student[0] + " " + student[1] + " has received a Thanos Gauntlet.")
                    i=i+1
            except:
                my_connect.rollback()
                mb.showerror("Failed", "Top winner could not be found")


        self.topWinnerButton = customtkinter.CTkButton(master = self.frame_right, text = 'Top Winner', command=showTopWinner)
        self.topWinnerButton.place(relx = 0.1, rely = 0.13)

        self.prize1 = ImageTk.PhotoImage(Image.open("Pictures/gauntlet.jpg"))
        self.prize2 = ImageTk.PhotoImage(Image.open("Pictures/tshirt.jpg"))
        self.prize3 = ImageTk.PhotoImage(Image.open("Pictures/gcard.jpg"))

 
        self.gauntletlabel = Label(master=self.frame_right, image=self.prize1, bg = '#d1d5d8')
        self.gauntletlabel.place(relx = 0.2, rely = 0.572, anchor = 'center')

        self.tshirtlabel = Label(master=self.frame_right, image=self.prize2, bg = '#d1d5d8')
        self.tshirtlabel.place(relx = 0.47, rely = 0.75, anchor = 'center')

        self.cardlabel = Label(master=self.frame_right, image=self.prize3, bg = '#d1d5d8')
        self.cardlabel.place(relx = 0.47, rely = 0.4, anchor = 'center')


        def showRandomWinner(): # This function uses a random number generator to find a random student per grade level
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            try:
                randomWinners = ""
                my_conn = my_connect.cursor()
                my_conn.execute("select FirstName, LastName, Grade from student where grade=9 ORDER BY RAND() Limit 1")
                
                i=0 
                for winner in my_conn:
                    randomWinners = "9th Grade Winner: " + winner[0] + " " + winner[1] + "\n"
                    i=i+1

                my_conn.execute("select FirstName, LastName, Grade from student where grade=10 ORDER BY RAND() Limit 1")
                
                i=0 
                for winner in my_conn:
                    randomWinners += "10th Grade Winner: " + winner[0] + " " + winner[1] + "\n"
                    i=i+1

                my_conn.execute("select FirstName, LastName, Grade from student where grade=11 ORDER BY RAND() Limit 1")
                
                i=0 
                for winner in my_conn:
                    randomWinners += "11th Grade Winner: " + winner[0] + " " + winner[1] + "\n"
                    i=i+1

                my_conn.execute("select FirstName, LastName, Grade from student where grade=12 ORDER BY RAND() Limit 1")
                
                i=0 
                for winner in my_conn:
                    randomWinners += "12th Grade Winner: " + winner[0] + " " + winner[1]
                    i=i+1

                mb.showinfo("Random Winners", randomWinners + "\n\n" + "Our AAI Grade Winners have received a $10 Starbucks Gift Card as well as AAI Spirit Wear.")
            except:
                my_connect.rollback()
                mb.showerror("Failed", "Random winner could not be found")


        self.randomWinnerButton = customtkinter.CTkButton(master = self.frame_right, text = 'Random Winner', command=showRandomWinner)
        self.randomWinnerButton.place(relx = 0.4, rely = 0.13)

        # The following fields are check boxes that allow the user to customize their output reports
        fNameVar = tk.StringVar()
        lNameVar = tk.StringVar()
        ageVar = tk.StringVar()
        gradeVar = tk.StringVar()
        GPAVar = tk.StringVar()

        self.fNameCheck = ttk.Checkbutton(master = self.frame_right, text = 'Show First Name', onvalue='Show First Name', offvalue='Do Not Show First Name', variable=fNameVar)
        self.fNameCheck.place(relx = 0.7, rely = 0.25)

        self.lNameCheck = ttk.Checkbutton(master = self.frame_right, text = 'Show Last Name', onvalue='Show Last Name', offvalue='Do Not Show Last Name', variable=lNameVar)
        self.lNameCheck.place(relx = 0.7, rely = 0.35)

        self.GradeCheck = ttk.Checkbutton(master = self.frame_right, text = 'Show Grade', onvalue='Show Grade', offvalue='Do Not Show Grade', variable=gradeVar)
        self.GradeCheck.place(relx = 0.7, rely = 0.45)

        self.AgeCheck = ttk.Checkbutton(master = self.frame_right, text = 'Show Age', onvalue='Show Age', offvalue='Do Not Show Age', variable=ageVar)
        self.AgeCheck.place(relx = 0.7, rely = 0.55)

        self.GPACheck = ttk.Checkbutton(master = self.frame_right, text = 'Show GPA', onvalue='Show GPA', offvalue='Do Not Show GPA', variable=GPAVar)
        self.GPACheck.place(relx = 0.7, rely = 0.65)

        self.pointsCheck = ttk.Checkbutton(master = self.frame_right, text = 'Show Total Points', onvalue='Show Total Points', offvalue='Do Not Show Total Points', state='disabled')
        self.pointsCheck.place(relx = 0.7, rely = 0.75)

        def showQuarterlyReport(): # This function shows a table that can be changed based upon the checkboxes above and displays a report of the students
            my_w = tk.Tk()
            my_connect = mysql.connector.connect(
            host="localhost",
            user="root", 
            passwd="Aai#1Database",
            database="studentdb"
            )

            my_conn = my_connect.cursor()
            ReportSelection = ""
        
            if fNameVar.get() == "Show First Name":
                ReportSelection += "s.FirstName,"

            if lNameVar.get() == "Show Last Name":
                ReportSelection += "s.LastName,"

            if gradeVar.get() == "Show Grade":
                ReportSelection += "s.Grade,"

            if ageVar.get() == "Show Age":
                ReportSelection += "s.Age,"

            if GPAVar.get() == "Show GPA":
                ReportSelection += "s.GPA,"

            my_conn.execute("select " + ReportSelection + " count(et.StudentID) as TotalPoints from eventtracker et inner join student s on et.StudentID=s.StudentID group by et.StudentID order by s.Grade, s.FirstName, s.LastName")

            i=1
            for student in my_conn: 
                for j in range(len(student)):
                    e = Entry(my_w, width=15, fg='blue') 
                    e.grid(row=i, column=j) 
                    e.insert(END, student[j])
                i=i+1

        self.reportButton = customtkinter.CTkButton(master = self.frame_right, text = 'Generate Quarterly Report', command=showQuarterlyReport)
        self.reportButton.place(relx = 0.7, rely = 0.13)

class studentView(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
  
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        
        self.titleLabel = ttk.Label(master=self.frame_right,
                                              text="Welcome Student",
                                              font=("Roboto Medium", 20),
                                              background='#d1d5d8')
        self.titleLabel.place(relx = 0.5, rely = 0.07, anchor='center')

        # Name Fields

class logInView(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
  
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        
        self.titleLabel = ttk.Label(master=self.frame_right,
                                              text="Welcome To the Alliance Event Tracker!",
                                              font=("Roboto Medium", 30),
                                              background='#d1d5d8')
        self.titleLabel.place(relx = 0.5, rely = 0.07, anchor='center')

        self.instructionsLabel = ttk.Label(master=self.frame_right,
                                            text= "Please Log In With Your ID and Password",
                                            font=("Roboto Medium", 15),
                                            background='#d1d5d8')
        self.instructionsLabel.place(relx = 0.5, rely = 0.2, anchor='center')

        self.logInLogo = ImageTk.PhotoImage(Image.open("Pictures/logo.png"))
        self.logInLogo_Label = Label(master=self.frame_right, image=self.logInLogo, bg = '#d1d5d8')
        self.logInLogo_Label.place(relx=0.1, rely= 0.15)    

def on_closing(self, event=0):
        self.destroy() 

app = tkinterApp()
app.mainloop()
