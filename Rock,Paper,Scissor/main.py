#                              Rock, Paper and Scissor

import random                #We have to make sure we import random

"""
1 for rock
-1 for paper
0 for scissor
"""
computer = random.choice([-1,0,1])  #This makes sure computer makes random choice
youstr = input("Enter your choice: ")
youDict = {"r":1, "p":-1, "s":0}
reverseDict = {1:"Rock",-1:"Paper",0:"Scissor"}

you = youDict[youstr]

#By now we have 2 number (variables) you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if (computer == you):
    print("It's a draw")

else:

    """This is the alternate short version by applying complex/creative logic"""
    #if((computer - you) == -1 or (computer - you) == 2 ):
       # print("You lose")
        #else:
            #print("You win")

         
    if(computer == -1 and you ==1):
        print("You win")
 
    elif(computer == -1 and you ==0):
        print("Computer win")

    elif(computer == 1 and you ==-1):
        print("Computer win")

    elif(computer == 1 and you ==0):
        print("You win")

    elif(computer == 0 and you ==-1):
        print("You win")

    elif(computer == 1 and you ==0):
        print("Computer win")   

    else:
        print("Something wrong,try again")                     
        




