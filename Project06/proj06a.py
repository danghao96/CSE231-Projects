###############################################################################
#   Computer Project #6a
#
#   This program will read the contents of a user-selected data file and will 
#   call function “draw_graph” to plot a graph of the data from that file.
#   The program will prompt the user for the name of the input file.  If it is 
#   unable to open that file, the program will display an appropriate message 
#   and halt. The program will read the contents of that file and store the 
#   values in two lists, then call function “draw_graph” to draw a graph. The 
#   data file will contain zero or more lines, where each line contains a year
#   (4 characters), a space, and a temperature deviation (4 characters).

###############################################################################

import pylab

def draw_graph( x, y ):
    '''Plot x vs. y (lists of numbers of same length)'''

    # Title for the graph and labels for the axes
    pylab.title( "Change in Global Mean Temperature" )
    pylab.xlabel( "Year" )
    pylab.ylabel( "Temperature Deviation" )

    # Create and display the plot
    pylab.plot( x, y )
    pylab.show()


def open_file():
    """
    Open the file specified by user.
    Returns: If the file exists, returns the file name (file).
    If the file does not exist, return the error message "error" (str)
    """
    # Return the file name if the file exists.
    try:
        file_name = input("Please enter the file name:")
        file_in = open(file_name, "r")
        return file_in
    
    # if user input a file that does not exist, return the error message
    except FileNotFoundError:
        return "error"

def process_file(file_in):
    """
    Read the file and get the year and temperature values from file, then, 
    store them in two lists.
    file_in: the input file (file)
    Returns: Return the year (list) and temperature (list) in tuple
    """
    # Initialize lists
    year = []
    temp = []
    
    # Loop to read file
    for line in file_in:
        year.append(int(line[0:4])) # Get year values and stored in list
        temp.append(int(line[5:9])) # Get temperature values and stored in list
        
    return(year, temp) #Return lists
    
def main():
    """
    Call functions and pass variavles between functions. Handle the error 
    message from file_in function.
    """
    
    file_in = open_file() #Call open_file() function to prompt user open a file
    
    # If statement to check if the function open_file returns an error message
    if file_in != "error":
        (x, y) = process_file(file_in) #Call process_file function to get lists
        draw_graph(x, y) #Call draw_graph function to graw a graph
        file_in.close() #Close file after finish reading
    else:
        #If open_file function returns an error message, prompt user and exit 
        #the program
        print("File not exists. Program Halted!")

# If there is any error occured unexpectly, prompt user and halt the program
try:
    main() #Call main function to run the program
except:
    print("Unknown Error! Program Halted!")