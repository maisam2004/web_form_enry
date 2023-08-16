import tkinter as tk
from tkinter import messagebox 
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
        self.name_entry = tk.Entry(self.root,width=40)
        self.name_entry.pack(padx=1,pady=1)

        tk.Label(self.root,text="Mobile:",font=("Arial",16)).pack(padx=4,pady=4)
        self.name_entry = tk.Entry(self.root,width=40)
        self.name_entry.pack(padx=1,pady=1)

        tk.Label(self.root, text="Post Code:",font=("Arial",16)).pack(padx=4,pady=4)
        self.postcode_entry = tk.Entry(self.root,width=40)
        self.postcode_entry.pack(padx=1,pady=1)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit",font=("Arial",14))
        self.submit_button.pack(padx=10,pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = FormApp(root)
    root.mainloop()