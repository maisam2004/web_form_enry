import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json,os.path

class DataEntryApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Data Entry Form")
        self.entries = {} #for dicitonary info appending
        self.setup_ui()
        if os.path.exists('1st_jfile.json'):
            self.load_entries_from_json()


    def load_entries_from_json(self):#to read file data if file exist
        try:
            with open('1st_jfile.json', 'r', encoding='utf8') as json_file:
                self.entries = json.load(json_file)
        except json.JSONDecodeError:
            self.entries = {}

    def setup_ui(self):
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.create_user_info_frame()
        self.create_courses_frame()
        self.terms_conditions_frame()

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

        self.submit_button = tk.Button(self.frame, text="Submit",fg="red", command=self.enter_data)
        self.submit_button.grid(row=3, column=0, pady=10)

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

    def terms_conditions_frame(self):
        #terms condition frame
        self.terms_frame = tk.LabelFrame(self.frame,text="Terms & Conditions")
        self.terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

        #variable for terms check box
        #terms_status = tkinter.BooleanVar(value=False)
        self.accept_var = tk.StringVar(value="Not accepted")
        self.terms_check =tk.Checkbutton(self.terms_frame,text="I accepts the terms and conditions.",variable=self.accept_var,onvalue='Accepted',offvalue="Not accepted")
        self.terms_check.grid(row=0,column=0)





    def enter_data(self):
        terms = self.accept_var.get()

        if terms == "Accepted":
            fname = self.first_name_entry.get()
            lname = self.last_name_entry.get()
            if fname and lname:
                title = self.title_combobox.get()
                age = self.age_spinbox.get()
                national = self.nationality_combobox.get()
                numcourses = self.numcourses_spinbox.get()
                numsemesters = self.numsemesters_spinbox.get()
                registration_status = self.reg_status_var.get()
                now = datetime.now()
                whole_text_info = ("- -" * 20) + '\n'
                whole_text_info += f'{now:%M:%S} \n first name : {fname} , last name = {lname=}, \n rgistery status ={registration_status}  age : {age} natinality :{national} \n'
                whole_text_info += "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
                dict_info = {
                        'title': title,
                        'first name': fname,
                        "last name": lname,
                        'age': age,
                        'nationality': national,
                        'registery status': registration_status,
                        'course number': numcourses,
                        'semester number': numsemesters,
                    }
                
                self.entries[f'{lname} {fname}']=(dict_info)

                with open('1st_jfile.json', 'w', encoding='utf8') as json_file:
                    json.dump(self.entries, json_file, ensure_ascii=False, indent=4)

                with open('new_file_class.txt', '+a') as Textfile:
                    print(whole_text_info, file=Textfile)

                self.first_name_entry.delete(0, tk.END)
                self.last_name_entry.delete(0, tk.END)
                self.title_combobox.set('')
                self.age_spinbox.delete(0, tk.END)
                self.nationality_combobox.set('')
                self.reg_status_var.set('NOT Registered')
                self.numcourses_spinbox.delete(0, tk.END)
                self.numcourses_spinbox.insert(0, "0")
                self.numsemesters_spinbox.delete(0, tk.END)
                self.numsemesters_spinbox.insert(0, "0")

                self.accept_var.set("Not accepted")

                
            else:
                messagebox.showerror(title="Names Error", message="Please enter first and last name!")
        else:
            messagebox.showinfo(title="Error", message="You have not accepted terms and conditions")


if __name__ == "__main__":
    window = tk.Tk()
    app = DataEntryApp(window)
    window.mainloop()
