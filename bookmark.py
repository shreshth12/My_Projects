import tkinter as tk
import webbrowser

def Facebook(event): 
    webbrowser.open_new_tab("https://www.facebook.com")
def Youtube(event):
    webbrowser.open_new_tab('https://www.youtube.com')
def Gmail(event):
    webbrowser.open_new_tab('https://www.gmail.com')
def custom_address():
    if Entry_1.index("end") == 0:
        pass
    else:
        webbrowser.open_new_tab(Entry_1.get())
    
window = tk.Tk()
window.title("GUI App by Shreshth") #To put the title
window.configure(background = "Black") #To change colour
window.geometry("650x200+800+400") #800-->xaxis and 400-->yaxis # it's where the program gets loaded

#big_entry_field = tk.Text(master=window,height=7,width=30)
#big_entry_field.grid(column=1,row=7)
#big_entry_field.insert(tk.END,"Type your text here")



label = tk.Label(text="Facebook",bg="Blue",font="None 16 bold underline",fg="white") #The number 20 says size # FG changes font colour
label.grid(column = 0 ,row=0)

label_1 = tk.Label(text="Youtube",bg="Red",font ="Arial 16 underline bold") #bg stands for background
label_1.grid(column=1,row=0)

label_2 = tk.Label(text="Gmail",font="None 16 underline bold")
label_2.grid(column=2,row=0)

guide = tk.Label(text="Click on the above links to redirect you to the respective page",fg='white',bg='black')
guide.grid(column = 1 ,row = 3)

button = tk.Button(window,text = "Open")
button.grid(column=0,row=1)

button_2 = tk.Button(window,text="Open") 
button_2.grid(column=1,row=1)

button_3 = tk.Button(window,text="Open") 
button_3.grid(column=2,row=1)

greeting=tk.Label(text='<-- Type here',font="None 26",fg='white',bg='black')
greeting.grid(column=1,row=5)
#------------------------------------------------------------------------------------------------
#For opening any custom page.
#Label for entry
Label_1 = tk.Label(text='Type the address you want to open',font="Arial 12 ",bg='black',fg='white')
Label_1.grid(column=0,row=4)

Entry_1 = tk.Entry()
Entry_1.grid(column=0,row=5)

Button_1 = tk.Button(window,text='Go',command=custom_address)
Button_1.grid(column=0,row=6)





button.bind("<Button-1>",Facebook) #Links the button to the actual function 
button_2.bind("<Button-1>",Youtube)
button_3.bind("<Button-1>",Gmail)

window.mainloop() # Runs the program
