import tkinter 
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




window.mainloop() #come up with it