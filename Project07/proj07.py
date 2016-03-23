###############################################################################
#   Computer Project #7
#
#   This program will calculate and display the inflation-adjusted cost of the 
#   congressional hearings. 
#   Firstly, this program will try to read the file inflation.txt and get the 
#   inflation value corresponding to each year and store these values in a list
#   secondly, this program will try to read the file hearings.txt and skip the 
#   first two lines. Then, the program will store the following lines in a list
#   Thirdly, this program will adjust the cost values obtained from the file 
#   hearings.txt based on the inflation values obtained from the file 
#   inflation.txt
#   Forthly, this program will read the file hearings.txt and store the name in
#   the name list, and store the cost in the cost list.
#   Fifthly, this program will call function draw_bar_graph to draw a graph by
#   the name list and cost lise.
#   Finally, this program will write the adjusted value into the file 
#   hearings_adjusted.txt
#  
###############################################################################

import pylab
def draw_bar_graph(x,y):
    '''Draw a bar graph of y values with labels from x where
       x is a list of strings; y is a list of values associated with each x'''
    number_of_bars = len(x)
    bar_width = 0.5
    # create a list (array) of indices for bars
    x_values = pylab.linspace(0,number_of_bars-1,number_of_bars)
    # associate a string label (tick) from x with each bar
    # orient the string to the middle of the bar, and rotate the label 45 
    # degrees
    pylab.xticks(x_values+bar_width/2, x, rotation=45)
    
    # Title for the graph and labels for the axes
    pylab.title( "Inflation-adjusted Cost for Hearings" )
    pylab.ylabel( "Cost (in millions of 2015 dollars)" )
    
    pylab.bar(x_values,y,width=bar_width)
    pylab.show()
	
def get_cols_from_file( file_name, column_list, ignore_number ):
    """
    This function reads a file, skips past a specified number of header lines, 
    reads values in specified columns, and returns a list of lists where each 
    nested list corresponds to the values read from one line of the file.
    file_name: the file name to read from (str)
    column_list: a list of integers defining the columns to be read (list)
    ignore_number: the number of header lines to ignore (int)
    Return: This function will return a list of lists, where the nested lists 
    contain the data from the specified columns, in the order specified by the 
    second parameter.
    """
    # open the file
    file_in = open( file_name, "r" )
    
    # initialize the lists and variable
    list_line_result = []
    result_list = []
    i = 0
    
    # for loop to read lines in the file and process the data from file
    for line in file_in:
        # if statement for ignoring the header lines
        if i >= ignore_number:
            list_line = line.split()
            # for loop to read the specific data from line
            for j in range( len( column_list ) ):
                index = column_list[j]      # get the index from column_list
                data = list_line[index]     # get data from list_line by index
                list_line_result.append( data )     # append data to the list 
                                                    # of data line
            result_list.append( list_line_result )  # append the list of data 
                                                    # line to the result list
            list_line_result = []   # empty the list of the data line
        i += 1
    return result_list # return the result line
    
    file_in.close() # close the file when finished the work

def find_index( year, inflation_list ):
    """
    This function will find the index in the inflation_list of the (nested) 
    list containing the inflation information for the given year.
    year: The year value that will be searched for the index (int)
    inflation_list: The inflation list for searching.
    Return: This function will return the index, in the input list, of the 
    nested list that indicates the inflation value for that year.
    """
    # for loop to go through every items in the list for searching
    for i in range( len(inflation_list) ):
        # if statement compare the first element of the nested list with the 
        # year value
        if inflation_list[i][0] == year: # if equal, return the current index 
                                         # number
            return i # return the current index number
            break

def adjust_for_inflation( amount, year, inflation_list ):
    """
    This function will adjust the amount for inflation from the specified year 
    to the present.
    amount: the original dollar amount (float)
    year: the year corresponding to the dollar amount (int)
    inflation_list: a list of lists of ints of years and inflation values for 
    the last 100 years (list)
    Return: This function will return the inflation-adjusted value of amount 
    (float) in year (int).
    """
    # define the constants
    PERCENT_CONVERTION = 0.01
    PRESENT_YEAR = 2015
    # initialize the variables
    index = find_index( year, inflation_list )
    index_present = find_index( PRESENT_YEAR, inflation_list )
    i = 0
    
    # for loop to read each elements in the inflation_list
    for element in inflation_list:
        
        inflation = element[1] * PERCENT_CONVERTION # convert the inflation to 
                                                    # percent value
        # read the inflation value in the index range from the index of input 
        # year to the index of present year.
        if index < i < index_present:
            amount *= 1 + inflation     # calculate the amount with the 
                                        # inflation for each year
        i += 1
    
    result = round(amount, 1)   # round the result to one deciaml place
    return result # return the result

def strlist_convert( list_in ):
    """
    This function convert the list of string lists to the list of float lists 
    with the first element in the lists as int.
    list_in: the list that contain string lists need to be converted (list)
    Return: This function will return the list of lists with first value as int
    and others as float.
    """
    result_list = []
    for element in list_in:
        list_element = list( map( float, element ) )
        list_element[0] = int( list_element[0] )
        result_list.append( list_element )
    return result_list

def file_to_list( file_name, ignore_number ):
    """
    This function will read the file and store the file in a list of lists.
    file_name: the file to read (str)
    ignore_number: the number of lines from beginning to ignore (int)
    Return: This function will return the list of lists that contain the content
    of the file.
    """
    # open the file
    file_in = open( file_name, "r" )
    
    # initialize the list and variable
    result_list = []
    i = 0
    
    # for loop to read lines in the file and process the data from file
    for line in file_in:
        # if statement for ignoring the header lines
        if i >= ignore_number:
            list_line = line.split() # split line in elements of list
            result_list.append( list_line ) # store the splited line in a list
        i += 1
    return result_list # return the result line
    
    file_in.close() # close the file when finished the work

def write_file( result_list ):
    """
    This function write the result_list into the file "hearings_adjusted.txt" 
    that has the same format as "hearings.txt" file.
    result_list: the result that will be writen in the file (list)
    """
    file_out = open("hearings_adjusted.txt", "w") # open the file as write
    # write the header into the file
    print("         Congressional Hearing Cost", file=file_out)
    print("Name         Cost ($Million)         Year", file=file_out)
    # for loop to write the list in the file element by element
    for element in result_list:
        print(element[0].ljust(12), str( element[1] ).rjust(4), \
        str( element[2] ).rjust(25), sep="", file=file_out)
        
    file_out.close() # close the file when finished

def main():
    """
    The main function mainly used to call other functions and to pass variables
    between functions
    """
    # call function get_cols_from_file to get the initial inflation list
    ini_inflation_list = get_cols_from_file( "inflation.txt", [0, -1], 1 )
    # call function strlist_convert to convert the type of element in the 
    # initial inflation_list to the approprate type
    inflation_list = strlist_convert( ini_inflation_list )
    # initialize lists
    list_name = []
    list_cost = []
    
    # call function file_to_list to get the datas from file hearings.txt
    hearings_list = file_to_list( "hearings.txt", 2 )
    # for loop to adjust the value of the cost in hearings_list to the adjusted
    # cost value.
    for element in hearings_list:
        # call function adjust_for_inflation to adjust the value of cost and 
        # assign the adjusted value to list
        element[1] = adjust_for_inflation( float( element[1] ), \
        int( element[2] ), inflation_list )
        
        # get the name list and cost list for drawing graph
        list_name.append(element[0])
        list_cost.append(element[1])
    
    # call function draw_bar_graph to draw the graph
    draw_bar_graph( list_name, list_cost )
    # call function write_file to write the hearings_list into the file
    write_file( hearings_list )

main()