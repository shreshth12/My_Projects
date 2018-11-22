import tkinter as tk
from random import randint


result_text =''
global Pick
Pick = ''

global Computer_SCORE
global Human_SCORE

Computer_SCORE = 0
Human_SCORE = 0


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PROGRAMMING >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def indentifier_R(event):
    global Pick
    Pick = ''
    Pick += 'ROCK'
    

def indentifier_P(event):
    global Pick
    Pick = ''
    Pick += 'PAPER'
    

def indentifier_S(event):
    global Pick
    Pick = ''
    Pick += 'SCISSOR'
    

def result_updator():
    global Human_SCORE
    global Computer_SCORE

    if Human_SCORE > Computer_SCORE:
        result.config(text='You won the game!')
    
    elif Human_SCORE == Computer_SCORE:
        result.config(text='That was a tie!')
    
    else:
        result.config(text='Computer won!')

def ALL_IN_ONE():
    def computer_choice_updator():
        global Computer_Moves
        Moves = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}
        Computer_Choice = randint(1, 3)
        Computer_Moves = Moves[Computer_Choice]
        
        Computer.delete(0, 'end')
        Computer.insert(0, Computer_Moves)

    def human_choice_updator():
        global Pick
        Human.delete(0,'end')
        Human.insert(0,Pick)

    def WINNER():
        global Computer_Moves
        global Pick
        global Computer_SCORE
        global Human_SCORE

        if Pick == 'ROCK' and Computer_Moves == 'ROCK':
            pass
        elif Pick == 'ROCK' and Computer_Moves == 'PAPER':
            Computer_SCORE += 1
        elif Pick == 'ROCK' and Computer_Moves == 'SCISSORS':
            Human_SCORE += 1
        elif Pick == 'PAPER' and Computer_Moves == 'ROCK':
            Human_SCORE += 1
        elif Pick == 'PAPER' and Computer_Moves == 'PAPER':
            pass
        elif Pick == 'PAPER' and Computer_Moves == 'SCISSORS':
            Computer_SCORE +=1
        elif Pick == 'SCISSOR' and Computer_Moves == 'ROCK':
            Computer_SCORE += 1
        elif Pick == 'SCISSOR' and Computer_Moves == 'PAPER':
            Human_SCORE += 1
        elif Pick == 'SCISSOR' and Computer_Moves == 'SCISSORS':
            pass

    def score_updator():
        h_score.config(text=Human_SCORE)
        c_score.config(text=Computer_SCORE)

    human_choice_updator()
    computer_choice_updator()
    WINNER()
    score_updator()








#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#GUI for the game.

root = tk.Tk()
root.geometry("305x310+800+400")
root.configure(bg = 'grey11')
root.title('---------RPS----------')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   LABELS AND THEIR ENTRIES  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Top half portion
Above_Human = tk.Label(text="Your Choice",fg='white',bg='grey11',font='None 12 bold')
Above_Human.grid(column=0,row=0,padx=10,pady=10)

Human = tk.Entry()
Human.grid(column=0,row=1,padx=0,pady=0)
Human.config(bg='indian red',relief='raised',justify='center',bd=5,font='None 10 bold')

Above_Computer = tk.Label(text="Computer Choice",fg='white',bg='grey11',font='None 12 bold')
Above_Computer.grid(column=1,row=0,padx=10,pady=10)

Computer = tk.Entry()
Computer.grid(column=1,row=1,padx=0,pady=0)
Computer.config(bg='indian red',relief='raised',justify='center',bd=5,font='None 10 bold')

#-----------------------------------------------------------------------------------------------
#Lower half portion Rock , Paper , Scissor BUTTONS!

rock=tk.Button(root,text="   ROCK   ",font="None 12 bold",bg='grey50',fg='yellow',command=ALL_IN_ONE)
paper=tk.Button(root,text="  PAPER  ",font="None 12 bold",bg='grey50',fg='White',command=ALL_IN_ONE)
scissor=tk.Button(root,text="SCISSOR",font="None 12 bold",bg='grey50',fg='light green',command=ALL_IN_ONE)

rock.bind("<Button-1>",indentifier_R)
paper.bind("<Button-1>",indentifier_P)
scissor.bind("<Button-1>",indentifier_S)

rock.grid(column=0,row=2,pady=5)
paper.grid(column=0,row=3,pady=5)
scissor.grid(column=0,row=4,pady=5)

#------------------------------------------------------------------------------------------------
#Score board!

human_score = tk.Label(text="Human Score",font='None 12 bold underline',bg='grey11',fg='white')
human_score.grid(column=1,row=2)

h_score=tk.Label(text=Human_SCORE,font='None 12 bold',bg='grey11',fg='white')
h_score.grid(column=1,row=3)

computer_score =tk.Label(text="Computer Score",font='None 12 bold underline',bg='grey11',fg='white')
computer_score.grid(column=1,row=4)

c_score =tk.Label(text=Computer_SCORE,font='None 12 bold',bg='grey11',fg='white')
c_score.grid(column=1,row=5)

#------------------------------------------------------------------------------------------------
#Result!

result = tk.Label(text=result_text,font='None 12 bold',bg='grey11',fg='white')
result.grid(column=0,row=7)

end_game = tk.Button(text='END GAME',font='None 12 bold',bg='grey11',fg='white',command=result_updator)
end_game.grid(column=0,row=6,pady=5)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GUI ENDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
root.mainloop()
