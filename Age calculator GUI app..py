

import datetime
import tkinter as tk
from tkinter import ttk
window = tk.Tk() #tk is module and #Tk is an object
window.geometry("300x300+800+400") #Geometry is a method
window.title("Age calculator app") #Window is the object
class Person:
    def __init__(self, name , birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        Today = datetime.date.today()
        age = Today.year - self.birthdate.year
        return age

Object = Person("Freak",datetime.date(1999,8,20))
#print(Object.name)
#print(Object.birthdate)
#print(Object.age())
#window.configure(bg = "grey")
def calculate_age():
    Solution = Person("Anonymous",datetime.date(int(year_entry.get()),int(month_entry.get()),int(day_entry.get())))
    Real_Age = 0

    if int(month_entry.get()) <= 6 :
        Real_Age = int(Solution.age()) - 1
    else:
        Real_Age = int(Solution.age())

    #----------------------THIS IS FOR THE TEXT WIDGET
    widget = tk.Text(master=window, height=15, width= 25)
    widget.grid(column=1,row=6)
    #_______________________THIS IS FOR ALREADY DECIDED INPUT
    widget.insert(tk.END,"You are ")
    widget.insert(tk.END,Real_Age )
    widget.insert(tk.END, " years old. ")

    #-------------------------OR YOU CAN USE
    #answer="{name} is {age} years old.".format(name=Solution.name,age=Solution.age())
    #widget.insert(tk.END, answer)

#anything = ttk.Combobox(window,text = any_text)
#anything.grid(column=0,row=6)

year_label = tk.Label(text ="Year")
year_label.grid(column=0,row=3)

month_label =tk.Label(text ='Month')
month_label.grid(column=0,row=4)

day_label = tk.Label(text="Day")
day_label.grid(column=0,row=5)

year_entry =tk.Entry() #This entry creates the entry fields
year_entry.grid(column =1 ,row=3)

month_entry = tk.Entry()
month_entry.grid(column =1,row=4)

day_entry = tk.Entry()
day_entry.grid(column=1,row=5)

calculate = tk.Button(window, text='Calculate now', command = calculate_age)
calculate.grid(column=1,row=6)
#To add image
#only double slashes will work

#image = Image.open("C:\\Users\\shres\\Desktop\\Python\\CP\\pic.jpeg")
#image.thumbnail((100,100),Image.ANTIALIAS)

#photo = ImageTk.PhotoImage(image)
#label_image=tk.Label(image=photo)
#label_image.grid(column=1,row=1)


window.mainloop()
