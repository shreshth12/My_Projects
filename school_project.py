from random import randint
turn_on = 0

print("Welcome to the Rock, Paper and Scissors game!!")

while True:
  start = input("Shall we proceed ? (Y/N)  ")
  if start.upper() == 'Y':
    print('Game starts! Press anything else than 1 2 or 3 to end the game!')
    turn_on += 1
    break
    
  elif start.upper() == 'N':
    print('Game terminated')
    break
    
  else:
    print('You put a wrong variable , please select Y or N ,where Y corresponds to Yes and N corresponds to No ')

Computer_SCORE = 0
Human_SCORE = 0
    
if turn_on == 1:
    while True:
        List = [1,2,3]
        
        Moves = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}

        Computer_Choice = randint(1, 3)
        Computer_Moves = Moves[Computer_Choice]

        print('                                                                                                         ')
        your_choice = int(input("Choose : 1)Rock    2)Paper     3)Scissors : "))
        print('                                                                                                         ')
        if your_choice != 1 and your_choice !=2 and your_choice !=3 :
          if Human_SCORE > Computer_SCORE:
            print('You won the game!')
          elif Human_SCORE == Computer_SCORE:
            print('That was a tie!')
          else:
            print('Computer won!')
            
          break
        else:
            Pick  = Moves[your_choice]
        
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
            elif Pick == 'SCISSORS' and Computer_Moves == 'ROCK':
              Computer_SCORE += 1
            elif Pick == 'SCISSORS' and Computer_Moves == 'PAPER':
              Human_SCORE += 1
            elif Pick == 'SCISSORS' and Computer_Moves == 'SCISSORS':
              pass
            
            print( 'Your choice : ',Pick,'                 Computer choice :',Computer_Moves)                                                                         
            print('Your score : ',Human_SCORE,'                 Computer score : ',Computer_SCORE)
        

       
    
    
    
   
  
