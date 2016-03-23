###############################################################################
#   Computer Project #6b
#
#   The program in “proj06c.py” willread the file named “data_full.txt” and 
#   will display a list of the N warmest months in the data set, where N is an 
#   integer number selected by the user.
#   The program will always read from “data_full.txt” (it will not prompt the 
#   user for the name of the input file).  If it is unable to open that file, 
#   the program will halt.
#   The program will read the contents of “data_full.txt” and will create a 
#   list of tuples, where each tuple contains a year, a month and a temperature
#   deviation
#    The program will prompt the user to enter the number of months (N) which 
#   should be included in the list of warmest months.  If the user does not 
#   enter a positive integer value for N, the program will repeatedly display 
#   an appropriate message and prompt the user again (until the user enters a 
#   positive integer value).
#   The program will display a list of the N warmest months in the data set 
#   (based on the monthly temperature deviations).  The list will be displayed 
#   in sorted order, from largest to smallest. Each item in the list will 
#   include the year, month name and temperature deviation. 
#   The report will include a title and will be appropriately formatted.
#   The program will display appropriate messages to inform the user about any 
#   unusual circumstances.
#
###############################################################################
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

def get_int():
    """
    Get an integer from user. If user inputs a noninteger, print error message.
    Return: return the integer inputed by user.
    """
    try:
        i = int(input("input the number of months(Please input a positive \
integer):"))
        if i < 0:
            print("Input Error! Please enter a positive integer!")
            i = get_int()
    except:
        print("Input Error! Please enter a positive integer!")
        i = get_int()
    return i


def data_sort(list_data):
    """
    Sort the data list by temperature from big to small.
    list_data: the list of tuples that contain year, month, and temperature
    values (list). The function will rearrange the sequence of the list
    """
    i = 0 #Initialize the variable
    length = len(list_data) #Get the length of the data list
    
    #This is a bubble sort method.
    while length > 0: # If there still contain unsorted data, sort them
        # Loop to sort data
        for i in range(length - 1):
            
            # Exchange the position of two tuples if the first one is smaller
            # than the second one.
            if list_data[i][3] < list_data[i+1][3]:
                l = list_data[i]
                list_data[i] = list_data[i+1]
                list_data[i+1] = l
                
        length -= 1 #After one sort, unsorted list length minis one

def get_date_by_N(list_data):
    """
    Select the first Nth tuples from the list.
    list_data: This is a data list that has been sorted by temperatyre from big
    to small (list)
    Return: return the result (list) of first Nth tuples in a list
    """
    n = get_int() #Get the integer specified by user represent the months 
    # selected.
    
    result = [] # Initialize the result list.
    
    # If user enters a value that out of range of the data list, redifine the 
    # n value to the length of the list of data
    if n > len(list_data):
        n = len(list_data)
        print("Input value is larger than totle available datas, input value \
has been redifined to the number of total available datas")
    elif n == 0:
        print("Nothing selected, output empty.")
        
    # Loop to add tuples to the result list
    for i in range(n):
        result.append(list_data[i])
    return result
    
        
def process_file(file_in):
    """
    
    """
    # Initialize the lists and variavle
    list_data = []
    list_month = []
    result = []
    i = 0
    
    # Loop to read lines in file_in file
    for line in file_in:
        j = 0 # Initialize the variable every time read a new line
        s = line[5:].split() # Get the temperature values and store in a list
        
        # For the first line in the file, get the list of month
        if i == 0:
            list_month = s
        else: # For other lines in the file, Create the tuple to store the year,
        # month, and temperature.
            # Loop to create tuple of the data for one month and store the
            # tuple in a list.
            for element in s:
                T = int(line[0:4]), list_month[j], " ", int(s[j])
                list_data.append(T)
                j += 1
        i += 1

    data_sort(list_data) # Call function data_sort to sort the date
    result = get_date_by_N(list_data) # Call function get_data_by_N to get the
    # first Nth months data.
    print ("Temperature Report\nThe", len(result), "warmest months and their \
corresponding temperatures are:") # Print the title and introduction of the 
# report

    # Print the data line by line with approprate format.
    for data in result:
        for element in data:
            print (element, end=" ")
        print()

def main():
    """
    Call functions to run the program and pass variables between functions.
    Handle the error message generated by open_file function
    """
    file_in = open_file()
    if file_in != "ThisIsAnErrorMessage":
        process_file(file_in)
    else:
        print("File not exists. Program Halted!")

# If there is any unexpected errors occured, prompt user.
try:
    main()
except:
    print("Unknown error occured! Program halted!")