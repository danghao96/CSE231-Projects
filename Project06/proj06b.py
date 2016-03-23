###############################################################################
#   Computer Project #6b
#
#   This program will generate a file which can serve as the input file for 
#   the program in Part A.
#   The program will always read from “data_full.txt”. If it is unable to open 
#   that file, the program will halt. 
#   The program will prompt the user for the name of the output file. If that 
#   file does not exist, the program will create it and continue. If that file
#   does exist, the program will discard the current contents of the file and 
#   continue. 
#   The program will allow the user to select the subset of the data which is 
#   to be processed and written into the output file. 
#   The program will allow the user to select the subset of lines in 
#   “data_full.txt” which are to be processed.
#   The program will prompt the user to enter a year, and it will then prompt 
#   the user to enter an integer count. The year will identify the first year 
#   that the user wants to include in the subset, and the integer count will 
#   identify the number of years that the user wants to include in the subset.
#   If the user enters an integer count which is greater than the number of 
#   years available, the program will include as many years as possible in the
#   subset. 
#   If the user enters "all" (any mix of upper and lower case letters) as the 
#   year, the program will include the entire data set as the subset to be 
#   processed; it will not prompt the user to enter an integer count.
#   The program will calculate the average temperature deviation for each year 
#   in the selected subset:  it will calculate the sum of the 12 monthly 
#   temperature deviations for that year, divide by 12, and round the resulting
#   value to 0 decimal places.
#   The program will then write the year and average temperature deviation to 
#   the output file using the format described in Part A.
#   The program will display appropriate messages to inform the user about any
#   unusual circumstances.
#
###############################################################################
import sys

def open_file():
    """
    Open the file "data_full.txt" and return "error".
    Returns: If the file exists, returns the file name (file).
    If the file does not exist, return the error message "error" (str)
    """
    try:
        file_in = open("data_full.txt", "r")
        return file_in

    except:
        return "ThisIsAnErrorMessage"
        

def new_file():
    """
    Open or create the output file specified by user.
    Returns: Returns the name for the output file specified by user (file)
    """
    
    file_name = input("Please enter the name for the output file:")
    file_out = open(file_name, "w")
    return file_out

def write_file(file_out, year, tem):
    """
    Write the output content into the output file.
    file_out: the name of the output file (file)
        Write the year (int) and cooresponding temperature (list) into the 
        file_out file (file)
    year: the value of the first year for the output date (int)
        Must be a 4-digit positive integer
    tem: the average temperature for each year (list)
    """
    # Loop to read data in tem list
    for tem_ave in tem:
        tem_ave = str(tem_ave).rjust( 4 ) #Format the average temperature value
        print(year, tem_ave, file=file_out, sep=" ") #Write in file
        year += 1 #year value plus one.

def get_count():
    """
    Get the value of count specified by user.
    If user inputs an error value, prompt user to enter again.
    Returns: Returns the count value (int)
    """
    try:
        count = int(input("Please enter a count:"))
    except:
        print("Input Error! Please enter an integer!")
        count = get_count()
    return count

def process_file(file_in):
    """
    Process the file. Process data selected by user. Calculate the average 
    temperature for each year selected by user. 
    Get the year values specified by user (str)
        If user inputs "all" (any mix of upper and lower case letters), read
        all lines (str) from file_in (file). Otherwise, read the lines match 
        the year (int) value entered by user,
    file_in: the input file (file)
    Returns: Returns year (int) and corresponding average temperature (list) 
    (tuples)
    """
    year = input("Please enter the year:") # Get the year value 
    
    # Initialize all variables and lists.
    tem_list = []
    tem_ave = 0
    tem = []
    i = 0
    
    # If user inputs "all" (any mix of upper and lower case letters) as a year 
    # value, process the entire file.
    if year.lower() == "all":
        
        # Loop to read lines in file_in
        for line in file_in:
            if line[0:4].isdigit(): # Ignore the invalid line.
                tem_list = line[7:].split() # Read the temperature for each month
                # and stored them in a list.
                tem_list = list(map(int, tem_list)) # Turn the string value in
                # list to int.
                tem_ave = int(round(sum(tem_list) / 12, 0)) # Calculate the 
                # average temperature for each year.
                tem.append(tem_ave) # Store the average temperature in a list.
                
                # Get the first year in the file.
                if i == 0:
                    year = int(line[0:4])
                i += 1
    
    # If user input a 4-digit integer as a year, read the selected data from 
    # the file.
    elif year.isdigit() and len(year) == 4:
        year = int(year) # Convert year value to integer
        count = get_count() # Call get_count function to get the count

        for line in file_in: # Loop the read lines in file_in
            if line[0:4].isdigit(): # Ignore the invalid line.
                if year <= int(line[0:4]) < year + count: # Read the line with
                # year calue within the range specified by user,
                    tem_list = line[7:].split() # Read the temperature for each
                    # month and stored them in a list.
                    tem_list = list(map(int, tem_list)) # Turn the string value
                    # in list to int.
                    tem_ave = int(round(sum(tem_list) / 12, 0)) # Calculate the 
                    # average temperature for each year.
                    tem.append(tem_ave)#Store the average temperature in a list
                    
                     # Get the first year in the file.
                    if i == 0:
                        # If the user inputs a year that is smaller than the 
                        # smallest year in the file, reset the input year as the 
                        # smallest year in file.
                        if year < int(line[0:4]):
                            year = int(line[0:4])
                            print("Input year is smaller than the smallest \
year in the file, the input year is reseted as the smallest year in file")
                    i += 1
            
    # If user inputs an invalid year value, prompt user to try again.
    else:
        sys.exit()
            
    
    # If no information was found, print the message to inform user.
    if tem == []:
        print("Information not found! Empty output file generated!")
    
    return(year, tem)


def main():
    """
    Call other functions and pass values between other functions.
    Catch errors from functions.
    """
    file_in = open_file()
    if file_in != "ThisIsAnErrorMessage": # If file_in function does not return
    # an error message, continue the program
        file_out = new_file()
        try:
            (year, tem) = process_file(file_in)
            write_file(file_out, year, tem)
            file_in.close()
            file_out.close()
        except:
            print("Input Error! Please enter a 4-digit number as a year! \
Program halted")
    else: # If file_in function does not return an error message, print the 
    # message and halt the program.
        print("File not exists. Program Halted!") # Print the error message

# If there is any unexpected errors occured, prompt user.
try:
    main()
except:
    print("Unknown error occured! Program halted!")