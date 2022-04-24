import math
import random


# Print the Matrix of the game .
def printCurrent(li):
    i=0
    print("-------------")
    for i in range(3):
        print("| ",end='')
        print(li[i][0],li[i][1],li[i][2],sep=" | ",end="")
        print(" |")
        print("-------------")

def makeAMove(li,choice,crntps):

    # Iterating every location one by one

    if crntps==0:
        if choice=='W' or choice=='w' or choice=='A' or choice=='a':
            print("You Wasted this move .")
        
        elif choice=='S' or choice=='s':
            li[0][0]=li[1][0]
            li[1][0]=' '
            return 3

        elif choice=='D' or choice=='d':
            li[0][0]=li[0][1]
            li[0][1]=' '   
            return 1

    elif crntps==1:
        if choice=='W' or choice=='w' :
            print("You Wasted this move .")

        elif choice=='S' or choice=='s':
            li[0][1]=li[1][1]
            li[1][1]=' '   
            return 4    

        elif choice=='A' or choice=='a':
            li[0][1]=li[0][0]
            li[0][0]=' ' 
            return 0

        elif choice=='D' or choice=='d':
            li[0][1]=li[0][2]
            li[0][2]=' '
            return 2

    elif crntps==2 :
        if choice=='W' or choice=='w' or choice=='D' or choice=='d':
            print("You Wasted this move .")

        elif choice=='A' or choice=='a':
            li[0][2]=li[0][1]
            li[0][1]=' '
            return 1

        elif choice=='S' or choice=='s':
            li[0][2]=li[1][2]
            li[1][2]=' '
            return 5

    elif crntps==3:
        if choice=='A' or choice=='a' :
            print("You Wasted this move .")  

        elif choice=='S' or choice=='s':
            li[1][0]=li[2][0]
            li[2][0]=' '
            return 6

        elif choice=='D' or choice=='d':
            li[1][0]=li[1][1]
            li[1][1]=' ' 
            return 4  

        elif choice=='W' or choice=='w':
            li[1][0]=li[0][0]
            li[0][0]=' ' 
            return 0 

    elif crntps==4 :

        if choice=='S' or choice=='s':
            li[1][1]=li[2][1]
            li[2][1]=' ' 
            return 7

        elif choice=='W' or choice=='w':
            li[1][1]=li[0][1]
            li[0][1]=' '  
            return 1                

        elif choice=='D' or choice=='d':
            li[1][1]=li[1][2]
            li[1][2]=' '  
            return 5

        elif choice=='A' or choice=='a':
            li[1][1]=li[1][0]
            li[1][0]=' '
            return 3

    elif crntps==5 :
        if choice=='D' or choice=='d' :
            print("You Wasted this move .")              

        elif choice=='A' or choice=='a':
            li[1][2]=li[1][1]
            li[1][1]=' '
            return 4

        elif choice=='W' or choice=='w':
            li[1][2]=li[0][2]
            li[0][2]=' '
            return 2
        
        elif choice=='S' or choice=='s':
            li[1][2]=li[2][2]
            li[2][2]=' '
            return 8


    elif crntps==6:
        if choice=='S' or choice=='s' or choice=='A' or choice=='a':
            print("You Wasted this move .")   

        elif choice=='W' or choice=='w':
            li[2][0]=li[1][0]
            li[1][0]=' '
            return 3
        
        elif choice=='D' or choice=='d':
            li[2][0]=li[2][1]
            li[2][1]=' '
            return 7

    elif crntps==7:
        if choice=='S' or choice=='s':
            print("You Wasted this move .")     

        elif choice=='W' or choice=='w':
            li[2][1]=li[1][1]
            li[1][1]=' '
            return 4
        
        elif choice=='A' or choice=='a':
            li[2][1]=li[2][0]
            li[2][0]=' '
            return 6
        
        elif choice=='D' or choice=='d':
            li[2][1]=li[2][2]
            li[2][2]=' '
            return 8

    elif crntps==8:
        if choice=='S' or choice=='s' or choice=='D' or choice=='d':
            print("You Wasted this move .")  

        elif choice=='A' or choice=='a':
            li[2][2]=li[2][1]
            li[2][1]=' '    
            return 7 
        
        elif choice=='W' or choice=='w':
            li[2][2]=li[1][2]
            li[1][2]=' '    
            return 5

    return crntps        



#  -----------------------------------Making the matrix random for starting of the game---------------------------

li= [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
    ]

# this represent the number which are not filled yet in the starting matrix
noFillednumber=[1,2,3,4,5,6,7,8]

# this represents the location which is not filled yet in the starting matrix
noFilledLocation=[0,1,2,3,4,5,6,7,8]

# Creating a random integer( range 1-8) filled matrix as a starting matrix 

while len(noFilledLocation)!=1:
    random_location=random.choice(noFilledLocation)

    random_number=random.choice(noFillednumber)

    # Extracting the location according to row and cols

    row=random_location//3
    col=random_location%3

    li[row][col]=random_number

    noFilledLocation.remove(random_location)
    noFillednumber.remove(random_number)

# Output sample matrix
sample=[
        [1,2,3],
        [4,5,6],
        [7,8,' '] ]

#--------------------------------Rules-------------------------------

print(" \n<------------------------------ Rules -------------------------------->\n")

print("Welcome to the game . You have  50 moves and you have to arrange the given  numbers like ")

printCurrent(sample)

print("\nRules ...\n1. W -> Upward   \n2. S -> Downward   \n3. A -> Left \n4. D -> Right ")

# crntps is used for keep a track of current postion (vacant position) which is  used for valid moves
crntps=random.choice(noFilledLocation)

movesLeft=50

#--------------------------------Games Starts-------------------------------

print(" \n<------------------------------ Game Starts -------------------------------->\n")

while movesLeft!=0:

    printCurrent(li)
    print("\n",movesLeft , " moves left" )
    choice=input("Enter the choice : ")

    while choice!='W' and choice!='w' and choice!='A' and choice!='a' and choice!='S' and choice!='s' and choice!='D' and choice!='d' :
        choice=input("Enter the correct key : ")

    crntps=makeAMove(li,choice,crntps)

    if li==sample:
        printCurrent(li)
        print("HIP HIP HURRY 🎊🎊🎊")
        print("You won the Game . ")
        quit()
    # Decreasing the move by one every time
    movesLeft=movesLeft-1

printCurrent(li)

print("You LOSE the game , Try next time .🥲🥲")