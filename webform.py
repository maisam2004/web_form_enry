from datetime import datetime
import tkinter as tk
from tkinter import messagebox 
from PIL import Image,ImageTk

class FormApp:
    def __init__(self,root):
        self.root = root
        self.root.title("User Info Form")

        self.root.geometry("650x550")
        self.create_form()
        ## adding image to background
        self.main_bg= ImageTk.PhotoImage(file="main_bg.jpg")
        bg=tk.Label(self.root,image=self.main_bg).place(x=10,y=0,relwidth=1,relheight=1)



### Register form by create frame
        frame1 = tk.Frame(self.root,bg="gray")
        frame1.place(x=60,y=20,width=480,height=420)
            ## lables and inputs inside of frame1
        first_name=tk.Label(frame1,text="Name:",font=("Arial",14,"bold"),fg="green").place(x=20,y=30)
        last_name=tk.Label(frame1,text="Last Name:",font=("Arial",14,"bold"),fg="green").place(x=250,y=30)

        self.first_name_entry = tk.Entry(frame1,width=30)
        self.first_name_entry.place(x=20,y=60)

        self.last_name_entry = tk.Entry(frame1,width=30)
        self.last_name_entry.place(x=220,y=60)
        


    def create_form(self):
        #lables
        tk.Label(self.root,text="Name:",font=("Arial",16)).pack(padx=10,pady=10)
        self.name_entry = tk.Entry(self.root,width=40)
        self.name_entry.pack(padx=1,pady=1)


        tk.Label(self.root,text="Family name:",font=("Arial",16)).pack(padx=4,pady=4)
        self.family_entry = tk.Entry(self.root,width=40)
        self.family_entry.pack(padx=1,pady=1)

        tk.Label(self.root, text="Address:").pack(padx=10,pady=10)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack(padx=1,pady=1)

        tk.Label(self.root,text="Mobile:",font=("Arial",16)).pack(padx=4,pady=4)
        self.mobile_entry = tk.Entry(self.root,width=40)
        self.mobile_entry.pack(padx=1,pady=1)

        tk.Label(self.root, text="Post Code:",font=("Arial",16)).pack(padx=4,pady=4)
        self.postcode_entry = tk.Entry(self.root,width=40)
        self.postcode_entry.pack(padx=1,pady=1)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit",font=("Arial",14),command=self.submit_form)
        self.submit_button.pack(padx=10,pady=30)

    def submit_form(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        mobile = self.mobile_entry.get()
        postcode = self.postcode_entry.get()

        if name and mobile:
            with open('web_form_info.txt','a') as file:
                now = datetime.now()
                message = f'you info /n {now:%M:%S} entries {name}/n{address}/n{mobile}'
                print(message,file=file)
            messagebox.showinfo('success',' file created')
            self.clear_form()
        else:#
            messagebox.showerror("Error ","please fill the form")


    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.family_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.postcode_entry.delete(0, tk.END)

        


if __name__ == "__main__":
    root = tk.Tk()
    app = FormApp(root)
    root.mainloop()