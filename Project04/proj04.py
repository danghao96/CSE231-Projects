###############################################################################
#   Computer Project #4
#
#   This python program will allow the user to decompress any number of strings.
#   The program will prompt for a string to decompress. If the user inputs a 
#   non-empty string, the program will output the decompressed string.
#   The program will display an error message and halt if the user inputs an 
#   empty string.
#
#   Algorithm
#   The program will first looks for a "(", a "," and a ")", than, the program
#   will read the number between the "(" and the ",", and the number between
#   the "," and the ")". Whit these two numbers, the program will locate the
#   text that represented by these two numbers. Then, the progran will replace
#   "(number1, number2)" with the text that represented by these two numbers.
#   This process will loop again and again until the whole text has been 
#   decompressed. Finally, the program will replace all "\\" with "\n" and 
#   display the decompressed text.
#
###############################################################################
#   Mail loop to allow user decompress text without reload the program.
while True:
    
    #   Prompt user to input the text or exit the program.
    user_input = input("Enter a string to decompress (or return to quit): ")
    
    #   Main if statement to judge if user inputs an empty string to exit.
    if user_input != "":
        
        #   Determine if the input text need to be decompressed or not.
        if "(" in user_input and "," in user_input and ")" in user_input:
            
            #   Initialize the variables.
            parenthesis_left = 0
            comma = 0
            parenthesis_right = 0
            
            #   If the unexpected value is in the parenthesis, prompt the user.
            try:
                
                # Loop to decompress all the texts that need to be decompressed
                while True:
                    
                    #   find positions of the two parenthesis and one comma
                    parenthesis_left = user_input.find("(", comma)
                    comma = user_input.find(",", parenthesis_left)
                    parenthesis_right = user_input.find(")", comma)
                    
                    #   judge if all parenthesises are replaced by texts.
                    if parenthesis_left >= 0:
                        
                        #   get two numbers in the parenthesis.
                        number_1 = int (user_input[parenthesis_left+1:comma])
                        number_2 = int (user_input[comma+1:parenthesis_right])
                        
                        #   Get the string of the whole parenthesis.
                        parenthesis = user_input[parenthesis_left:\
                        parenthesis_right+1]
                        
                        #   Get the text that represented by the parenthesis
                        substring = user_input[parenthesis_left-number_1:\
                        parenthesis_left-number_1+number_2]
                        
                        #   Replace the parenthesis with the text represented 
                        #   by the parenthesis.
                        output = user_input.replace(parenthesis, substring, 1)
                        user_input = output
                        
                        #   Go to next loop and decompress the next parenthesis
                        continue
                    
                    #   If all parenthesis was replaced by texts, replace the
                    #   "\" with "\n" in the entire input text.
                    else:
                        output = output.replace("\\", "\n")
                        
                        #   Print out the result.
                        print ("\nThe decompressed string prints as:")
                        print ("\n", output, sep="")
                        
                        #   Break the loop for decompress and waiting for next
                        #   input.
                        break
                    
            #   Handle the error of incorrect value in parenthesis.
            except ValueError:
                print ("The value in the parenthesis is wrong!")
                
        #   If the input only contain "\". replace them with "\n"
        elif "\\" in user_input:
            output = user_input.replace("\\", "\n")
            print ("\nThe decompressed string prints as:")
            print ("\n", output, sep="")
        
        #   If the input do not need to be decompressed, output the input.
        else:
            print ("Nothing to decompress, your input is:\n", user_input, \
            sep="")
    
    #   If user inputs an empty string, halt the program.
    else:
        print ("\nNothing to decompress. Exiting program.")
        break