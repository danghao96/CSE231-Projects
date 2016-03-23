###############################################################################
#   Computer Project #5a
#
#   This program will allow user copy select lines from "polio.txt" into a file
#   selected by user. User will select lines by year. A line is selected if the
#   user’s response matches the Year field or any of its prefixes.  All lines 
#   are selected if the user’s response is any of the values in the set 
#   {"","all","ALL"}
#
#   Algorithm
#   The program will first read the file "polio.txt" and then prompt user to 
#   enter a name for the output file. Then the program will prompt user to 
#   enter a command. If user enters "" or "all" or "ALL", the program will copy
#   all lines from "polio.txt" to the user spicified file. If user input a
#   number within 4 digits, the program will copy all lines with the year value
#   or its prefixes that matches the user response. If user inputs anything 
#   wrong, the program will prompt the user and exit.
#
###############################################################################
#   The main loop allows the error messages halt the program
while True:
    
    try:
        FILE = "polio.txt"
        file_in = open(FILE, "r")
    #If the file does not exist, prompt user and exit
    except FileNotFoundError:
        print("File not found, program halt!")
        break
    
    # Prompt user to input the name for output file and create that file.
    file_out_name = input("Input the name for output file:")
    file_out = open(file_out_name, "w")
    
    # Prompt user to input the command to search
    year_input = input("input the year to search or \"all\", \"All\", or \"\" \
    to copy the entire file:")
    
    try:
        # Judge if user input the command to copy the entire file.
        if year_input == "" or year_input == "all" or year_input == "ALL":
            # Copy the entire file
            for line in file_in:
                file_out.write(line)
        
        # If user do not inputs a command to copy the entire file, just assume
        # the user will search years for copy.
        else:
            year_len = len(year_input)  # Get the length of the input year
            year_int = int(year_input)  # Convert the input year to integer
            for line in file_in:
                # Search only those none empty line
                if line[68:68+year_len] != "":
                    # Get the year value from file
                    year = int(line[68:68+year_len])
                    
                    # If the year value from file matches the year value 
                    # entered by user, copy the corresponding line
                    if year == year_int:
                        file_out.write(line)
    
    # If the user did not input a valid command or a valid year value, let the 
    # user tru again.
    except ValueError:
        print("Input year error, please try again!")
        continue
    
    # Close the file after works done.
    file_in.close()
    file_out.close()
    break   #Stop the pregram.