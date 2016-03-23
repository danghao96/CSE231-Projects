###############################################################################
#   Computer Project #3
#
#   This python program is designed for Rock-Paper_Scissors game.
#   This program will allow users to play Rock-Paper_Scissors game against the
#   computer.
#
#   Algorithm
#   Display the rules first
#   Call function randint to generate the random number as computer's choice
#   Prompt user to input a command
#   Judge the command:
#       If the command is r, p, or s, compar it with computer's choice and
#       determine the winner. record the result.
#       If the command is q, display the statistic result and break the program
#       Otherwise, display error message and prompt the user to input again
#
#   Outputs:
#   After each round, output the computer's choice and user's choice, and
#   display the round result(Computer win, User win, or Tie)
#   After user input q to quit the game, display the statistic results:
#       How many times the user wins(and the percentage)
#       How many times the computer wins(and the percentage)
#       How many times the game ties(and the percentage)
#       How many times the user choose rock(and the percentage)
#       How many times the user choose paper(and the percentage)
#       How many times the user choose Scissors(and the percentage)
#
###############################################################################
import random
random.seed( 0 )

#Initialize the variables
count = 0
count_uwin = 0
count_cwin = 0
count_tie = 0
count_r = 0
count_p = 0
count_s = 0
percent_uwin = 0
percent_cwin = 0
percent_tie = 0
percent_r = 0
percent_p = 0
percent_s = 0
c_chose = ""

#Define some common string values for output
STR_UWIN = "User wins this round"
STR_CWIN = "Computer wins this round"
STR_TIE = "This round is a tie"

#Print the rules for the game
print ("Welcome to the Rock-Paper-Scissors game.")
print ("Enter a single character: r, s, p, or q to quit.")
print ("Rock beats Scissors which beats Paper which beats Rock.")

#Main loop for the program
while True:
    rand = random.randint(1,3)  #Generate the random value as computer's choice
    
    #Define the computer's choice as Rock, Paper, or Scissor
    if rand == 1:
        c_chose = "r"
    elif rand == 2:
        c_chose = "p"
    elif rand == 3:
        c_chose = "s"
        
    command = input ("Enter a command (rpsq): ") #Prompt user to input a command
    if command == "r":      #Judge the command
        count += 1          #Record the total times for round
        count_r += 1        #Record the user inputs
        
        #Compare user's choice with computer's choice
        if rand == 1:
            count_tie += 1      #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_TIE)
        elif rand == 2:
            count_cwin += 1     #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_CWIN)
        elif rand == 3:
            count_uwin += 1     #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_UWIN)
        continue                #Loop again for next round
    elif command == "p":        #Judge the command
        count += 1              #Record the total times for round
        count_p += 1            #Record the user inputs
        
        #Compare user's choice with computer's choice
        if rand == 1:
            count_uwin += 1     #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_UWIN)
        elif rand == 2:
            count_tie += 1      #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_TIE)
        elif rand == 3:
            count_cwin += 1     #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_CWIN)
        continue                #Loop again for next round
    elif command == "s":        #Judge the command
        count += 1              #Record the total times for round
        count_s += 1            #Record the user inputs
        
        #Compare user's choice with computer's choice
        if rand == 1:
            count_cwin += 1     #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_CWIN)
        elif rand == 2:
            count_uwin += 1     #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_UWIN)
        elif rand == 3:
            count_tie += 1      #Record the result
            #Print user's choice and result
            print ("User chose", command ,"and computer chose", c_chose)
            print (STR_TIE)
        continue                #Loop again for next round
    elif command == "q" and count != 0:     #Judge the command
        #Calculate the percentage of results and Round the percentage to one 
        #decimal point
        percent_uwin = round (count_uwin / count * 100, 1)
        percent_cwin = round (count_cwin / count * 100, 1)
        percent_tie = round (count_tie / count * 100, 1)
        percent_r = round (count_r / count * 100, 1)
        percent_p = round (count_p / count * 100, 1)
        percent_s = round (count_s / count * 100, 1)
        
        #Print the Statistics result
        print ("\nSummary statistics")
        print ("User wins: ", count_uwin, "(", percent_uwin, "%)")
        print ("Computer wins: ", count_cwin, "(", percent_cwin, "%)")
        print ("Ties: ", count_tie, "(", percent_tie, "%)")
        print ("\nUser statistics")
        print ("Rock: ", count_r, "(", percent_r, "%)")
        print ("Paper: ", count_p, "(", percent_p, "%)")
        print ("Scissors: ", count_s, "(", percent_s, "%)")
        break
    #If the user directly input q, prevent the program from being crash
    elif command == "q" and count == 0:     #Judge the command
        print ("\nSummary statistics")
        print ("User wins: ", count_uwin, "(", percent_uwin, "%)")
        print ("Computer wins: ", count_cwin, "(", percent_cwin, "%)")
        print ("Ties: ", count_tie, "(", percent_tie, "%)")
        print ("\nUser statistics")
        print ("Rock: ", count_r, "(", percent_r, "%)")
        print ("Paper: ", count_p, "(", percent_p, "%)")
        print ("Scissors: ", count_s, "(", percent_s, "%)")
        break
    #Print the error information and continue the program
    else:
        print("Error. Try again.")
        continue                #Loop again for next round
