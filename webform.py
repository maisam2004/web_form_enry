from datetime import datetime
import tkinter as tk
from tkinter import messagebox 
form PIL import Image,ImageTK

class FormApp:
    def __init__(self,root):
        self.root = root
        self.root.title("User Info Form")

        self.root.geometry("450x450")
        self.create_form()
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