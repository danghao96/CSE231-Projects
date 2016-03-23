###############################################################################
#   Computer Project #5b
#
#   This program will display a summary report to the user according to user's
#   command. The program will prompt user to enter the file name first to open
#   the file, then, the program will prompt user to enter the year and the 
#   income value. Then, the program will search the lines that match user's 
#   criteria and display the The count of records in the input file which match
#   the user’s criteria; The average percentage for those records (displayed 
#   with one fractional digit); The country with the lowest percentage for those
#   records; and The country with the highest percentage for those records.
#
#   Algorithm
#   
#
###############################################################################

# define a function to open a file
def open_file():
    try:
        file_name = input("Input the name:")
        file_input = open(file_name, "r")
        return file_input
    
    # if user input a file that does not exist, prompt user and try again
    except FileNotFoundError:
        print("File not exists. Please try again!")
        open_file() # Call the function again to try to open the file again

#   Define a function to convert the line from text to the text that can be 
#   understand by human.
def line_to_text(line):
    
    # Initialize the variables and give them string values
    income = line[0:6]
    region = line[7:11]
    country = line[12:67]
    year = line[68:72]
    percent = line[73:76]
    
    # Convert the income code to text
    if income == "WB_LI ":
        income = "low income"
    elif income == "WB_LMI":
        income = "lower middle income"
    elif income == "WB_UMI":
        income = "upper middle income"
    elif income == "WB_HI ":
        income = "high income"
    
    # Convert the region code to text
    if region == "AFR ":
        region = "Africa"
    elif region == "AMR ":
        region = "Americas"
    elif region == "EMR ":
        region = "Eastern Mediterranean"
    elif region == "EUR ":
        region = "Europe"
    elif region == "SEAR":
        region = "South-East Asia"
    elif region == "WPR ":
        region = "Western Pacific"
    
    country = country.strip() # delate the space in country code
    
    result = country + "\nThe World Bank income level is " + income + \
    "\nThe WHO region is " + region + "\nThe year is " + year + \
    "\nThe percentage vaccinated is" + percent + "%"

    return result

# Define the function to precess the file
def process_file( file_object ):
    
    # Initialize all the variables that will be used in this function
    count = 0
    income = ""
    income_input = ""
    year_input = ""
    country_low = ""
    country_high = ""
    percentage = 0
    percentage_ave = 0
    percentage_low = 0
    percentage_high = 0
    percentage_count = 0 
    percentage_round = 0
    
    # Prompt user to input the year and the income value for searching
    year_input = input("Please enter a year:")
    
    #If user input a not valid year, display error message and let user try 
    # again
    try:
        int(year_input)
    except ValueError:
        print("Year input not valid, please try again!")
        main()
    income_input = input("Please enter an income level(1, 2, 3, 4):")
    
    # Convert the input income value to code in order to compare with income
    # code in the file line.
    if income_input == "1":
        income = "WB_LI "
    elif income_input == "2":
        income = "WB_LMI"
    elif income_input == "3":
        income = "WB_UMI"
    elif income_input == "4":
        income = "WB_HI "
    else:
        # If user inputs an error value for income value, prompt user and let 
        # user try again
        print("Income level inputs error, please input 1, 2, 3, or 4")
        main()
    
    # a loop to read lines in file
    for line in file_object:
        
        # Judge if a line matches user's criteria, if so, process on this line.
        if year_input == line[68:72] and income == line[0:6]:
            percentage = int(line[74:76]) # Read the percentage of this line
            count += 1 #count the number of lines that matches user's criteria
            # Count the total percentage for calculating the acerage percentage
            percentage_count += percentage
            
            #Initialize the lowest percentage and the highest percentage
            if count == 1:
                percentage_low = percentage
                percentage_high = percentage
                
            # get the lowest value of percentage and get the country with the 
            # lowest percentage
            if percentage <= percentage_low:
                percentage_low = percentage
                country_low = line
                
            # get the highest value of percentage and get the country with the 
            # highest percentage
            if percentage >= percentage_high:
                percentage_high = percentage
                country_high = line
                
    percentage_ave = percentage_count / count #Calculate the average percentage
    percentage_round = round(percentage_ave, 1) #Round it to 1 decimal point
    
    # Call the function to convert the line from text to the text that can be 
    # understand by human.
    country_low = line_to_text(country_low)
    country_high = line_to_text(country_high)
    
    # Print out the result
    print("\nThe count of records in the input file which match the user’s \
criteria is ", count, "\nThe average percentage for those records is ", \
percentage_round, "%", sep = "")
    print("\nThe country with the lowest percentage for those records is", country_low)
    print("\nThe country with the highest percentage for those records is", country_high)
    
# Define the main function to call other functions to start the program
def main():
    file_object = open_file()
    process_file(file_object)
    
# Call main function to start the program
main()