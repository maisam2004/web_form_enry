import tkinter 
#import ttk module from tkinter for use list theme
from tkinter import ttk

window = tkinter.Tk() #name root window 
window.title("Data Entery form") #add title to window

frame = tkinter.Frame(window) #create frame inside window
frame.pack()
#create three lable frame in frame ,width and height ,3 rows and one column

user_info_frame = tkinter.LabelFrame(frame,text="User Information")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

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
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,stick="news",padx=20,pady=20)

window.mainloop() #come up with 