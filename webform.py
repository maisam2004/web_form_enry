import tkinter as tk
from tkinter import messagebox 
class FormApp:
    def __init__(self,root):
        self.root = root
        self.root.title("User Info Form")

        self.root.geometry("450x450")
    
    def create_form(self):
        #lables
        tk.Label(self.root,text="Name:",font=("Arial,18")).pack(padx=5,pady=5)

root = tk.Tk()
fform =FormApp(root)
root.mainloop()