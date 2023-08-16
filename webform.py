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
        tk.Label(self.root,text="Name:",font=("Arial",16)).pack()
        self.name_entry = tk.Entry(self.root,width=40)
        self.name_entry.pack(padx=1,pady=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = FormApp(root)
    root.mainloop()