import tkinter 
#import ttk module from tkinter for use list theme
from tkinter import ttk
from tkinter import messagebox
#to grab now time 
from datetime import datetime
import csv,json



#function for button clicked 
def enter_data():  # sourcery skip: extract-method
    terms = accept_var.get()

    if terms == "Accepted":
     
        fname= first_name_entry.get()
        lname= last_name_entry.get()
        if fname and lname:
            title= title_combobox.get()
            age = age_spinbox.get()
            national = nationality_combobox.get()
            #course info
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            registration_status = reg_status_var.get()
            now = datetime.now()
            whole_text_info = ("- -"*20)+'\n'  #short wersion for dash lines
            whole_text_info += f'{now:%M:%S} \n first name : {fname} , last name = {lname=}, \n rgistery status ={registration_status}  age : {age} natinality :{national} \n'
            whole_text_info += "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
            dict_info = {
                f'{lname} {fname}': {
                    'title': title,
                    'first name': fname,
                    "last name": lname,
                    'age': age,
                    'nationality': national,
                    'registery status': registration_status,
                    'course number': numcourses,
                    'semester number': numsemesters,
                }
            } 

            with open('1st_jfile.json','+a',encoding='utf8')as json_file:
                json.dump(dict_info,json_file,ensure_ascii=False,indent=4)

            with open('new_file.txt','+a')as Textfile:
                print(whole_text_info,file=Textfile)
                
            """
           




            with open('infos.csv','+a',newline='') as csvdata:
                infowriter = csv.writer(csvdata,delimiter=' ')
                infowriter.writerow(lname)
                infowriter.writerow(fname)
                infowriter.writerow(national)

            print(f'first_name ={fname} and last_name = {lname} title of him {title} with this age> {age} and funny nationality {national}' )
            print('number of courses ',numcourses,'and number of semesters = ',numsemesters,'reg status > ',registration_status)
            print("__ ____ ____ ___ ___ _ ____  ___ _ ____ ___ _ ___ __ ") """
        else:
            messagebox.showerror(title="names error" ,message="plaese enter first and last name !")
    else:
        #messagebox.showerror(title='untick terms',message="Please check term and conditions ")
        messagebox.showinfo(title="Error" ,message="You have not accepted terms and conditions ")
        


window = tkinter.Tk() #name root window 
window.title("Data Entery form") #add title to window

frame = tkinter.Frame(window) #create frame inside window
frame.pack()
#create three lable frame in frame ,width and height ,3 rows and one column

user_info_frame = tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=10)

#inside user info frame

first_name_lable = tkinter.Label(user_info_frame,text="First Name")
first_name_lable.grid(row=0 ,column=0)

last_name_lable = tkinter.Label(user_info_frame,text="Last Name")
last_name_lable.grid(row=0,column=1)

first_name_entry  = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)

last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1,column=1)

#list for user to select
title_lable= tkinter.Label(user_info_frame,text="Title")
title_combobox = ttk.Combobox(user_info_frame,values=[' ','MR.','MISS.','MRS.','DR.','PROF.'])
title_lable.grid(column=2,row=0)
title_combobox.grid(row=1,column=2)

#age lable
age_lable = tkinter.Label(user_info_frame,text='Age')
age_lable.grid(row=2,column=0)
#to create age spinbox 
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18 ,to=110)
age_spinbox.grid(row=3,column=0)

#create nationality input
nationality_lable = tkinter.Label(user_info_frame,text="Nationality")
nationality_lable.grid(row=2,column=2)

nationality_combobox =ttk.Combobox(user_info_frame,values=['indian',"bangali","turkey","uk"])

nationality_combobox.grid(row=3,column=2)

#to specify padding fro all parts inside of user info frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#second lable frame
courses_frame = tkinter.LabelFrame(frame,text="courses")
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

registered_lable = tkinter.Label(courses_frame,text="Registeration Status")
registered_lable.grid(row=0,column=0)

#create var to enable get checkbox click,and store in stringvar
reg_status_var = tkinter.StringVar(value="NOT Registerd")

registered_check = tkinter.Checkbutton(courses_frame,text="Currently Registered",variable=reg_status_var ,onvalue="Registered",offvalue="NOT Registerd")
registered_check.grid(row=1,column=0)

numcourses_lable = tkinter.Label(courses_frame,text="# Completed_courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame,from_=0,to="infinity")

numcourses_lable.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemesters_lable = tkinter.Label(courses_frame,text="# Semesters")
numsemesters_lable.grid(row=0,column=2)
numsemesters_spinbox = tkinter.Spinbox(courses_frame,from_=0,to="infinity" )
numsemesters_spinbox.grid(row=1,column=2)

#to specify padding fro all parts inside of user info frame
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


#test user info just for practice

""" second_users = tkinter.LabelFrame(frame,text="Second user",background='#e6f2ff')
second_users.grid(row=3,column=0,sticky="news",padx=10,pady=10)

fname = tkinter.Label(second_users,text="fname")
fname.grid(row=0,column=0)
fname_entry = tkinter.Entry(second_users)
fname_entry.grid(row=1,column=0)

ftitle = tkinter.Label(second_users,text="ftitle")
ftitle.grid(row=0,column=1)
books=['live','div','pre','code','colors','rainbox']
ftitle_entery = ttk.Combobox(second_users,values=books)
ftitle_entery.grid(row=1,column=1)

fnumyears_lable = tkinter.Label(second_users,text="fnum_years")
fnumyears_lable.grid(row=0,column=2)

fnumyears = tkinter.Spinbox(second_users,from_="1900",to="infinity")
fnumyears.grid(row=1,column=2)

for wid in second_users.winfo_children():
    wid.grid_configure(padx=10,pady=10) """
####end test user ifo
#terms condition frame
terms_frame = tkinter.LabelFrame(frame,text="Terms & Conditions")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

#variable for terms check box
#terms_status = tkinter.BooleanVar(value=False)
accept_var = tkinter.StringVar(value="Not accepted")
terms_check =tkinter.Checkbutton(terms_frame,text="I accepts the terms and conditions.",variable=accept_var,onvalue='Accepted',offvalue="Not accepted")
terms_check.grid(row=0,column=0)


#add button
button = tkinter.Button(frame,text="Enter data",fg="red",command=enter_data)
button.grid(row=4,column=0,sticky="news",padx=20,pady=20)
window.mainloop() #come up with 