import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json

class DataEntryApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Data Entry Form")

        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.create_user_info_frame()
        self.create_courses_frame()

    def create_user_info_frame(self):
        self.user_info_frame = tk.LabelFrame(self.frame, text="User Information")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10)

        tk.Label(self.user_info_frame, text="First Name").grid(row=0, column=0)
        tk.Label(self.user_info_frame, text="Last Name").grid(row=0, column=1)

        self.first_name_entry = tk.Entry(self.user_info_frame)
        self.first_name_entry.grid(row=1, column=0)

        self.last_name_entry = tk.Entry(self.user_info_frame)
        self.last_name_entry.grid(row=1, column=1)

        tk.Label(self.user_info_frame, text="Title").grid(row=0, column=2)
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=['', 'MR.', 'MISS.', 'MRS.', 'DR.', 'PROF.'])
        self.title_combobox.grid(row=1, column=2)

        tk.Label(self.user_info_frame, text="Age").grid(row=2, column=0)
        self.age_spinbox = tk.Spinbox(self.user_info_frame, from_=18, to=110)
        self.age_spinbox.grid(row=3, column=0)

        tk.Label(self.user_info_frame, text="Nationality").grid(row=2, column=2)
        self.nationality_combobox = ttk.Combobox(self.user_info_frame, values=['indian', "bangali", "turkey", "uk"])
        self.nationality_combobox.grid(row=3, column=2)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.enter_data)
        self.submit_button.grid(row=2, column=0, pady=10)

    def create_courses_frame(self):
        self.courses_frame = tk.LabelFrame(self.frame, text="Courses")
        self.courses_frame.grid(row=1, column=0, padx=20, pady=10)

        # Add widgets for courses frame here

        self.registered_lable = tk.Label(self.courses_frame,text="Registeration Status")
        self.registered_lable.grid(row=0,column=0)

        #create var to enable get checkbox click,and store in stringvar
        self.reg_status_var = tk.StringVar(value="NOT Registerd")

        self.registered_check = tk.Checkbutton(self.courses_frame,text="Currently Registered",variable=self.reg_status_var ,onvalue="Registered",offvalue="NOT Registerd")
        self.registered_check.grid(row=1,column=0)

        self.numcourses_lable = tk.Label(self.courses_frame,text="# Completed_courses")
        self.numcourses_spinbox = tk.Spinbox(self.courses_frame,from_=0,to="infinity")

        self.numcourses_lable.grid(row=0,column=1)
        self.numcourses_spinbox.grid(row=1,column=1)

        self.numsemesters_lable = tk.Label(self.courses_frame,text="# Semesters")
        self.numsemesters_lable.grid(row=0,column=2)
        self.numsemesters_spinbox = tk.Spinbox(self.courses_frame,from_=0,to="infinity" )
        self.numsemesters_spinbox.grid(row=1,column=2)

        for widget in self.courses_frame.winfo_children():
            widget.grid_configure(padx=10,pady=5)


    def enter_data(self):
        # Add your data entry code here
        pass

if __name__ == "__main__":
    window = tk.Tk()
    app = DataEntryApp(window)
    window.mainloop()
