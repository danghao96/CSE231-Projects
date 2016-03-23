###############################################################################
#   Computer Project #8
#
#   The program will display a menu which lists the following options:
#       A)  Read collection of contacts from file 
#       B)  Write collection of contacts to file 
#       C)  Add new contact 
#       D)  Remove existing contact 
#       E)  Update existing contact's phone number 
#       F)  Update existing contact's email address 
#       G)  Display contacts by prefix 
#       X)  Exit from the program
#
#   The user will select an option by entering the appropriate character 
#   (upper or lower case).  For example, the user will enter "A" (or "a") to 
#   select the first option (read contact list from file).
#
#   Option A will permit the user to read a collection of contacts from a file.
#   It will prompt the user for the complete name of the text file containing 
#   the collection of contacts.  The program will assume that the text file has
#   the following format:
#       name (character string) 
#       phone number (character string in the format DDD-DDD-DDDD) 
#       email address (character string in the format local@domain)
#   A semicolon will separate one field from the next field.
#   This option will clear all entries from the dictionary of contacts, then 
#   read the text file and insert each contact into the dictionary of contacts.
#   The contact's name will serve as the key for that contact's information 
#   (phone number and email address).
#
#   Option B will permit the user to write the collection of contacts to a 
#   file.  The program will prompt the user for the complete name of the text 
#   file to which the collection of contacts is to be written.  The program 
#   will write the contents of the dictionary of contacts into that text file, 
#   using the format given for Option A.
#
#   Option C will permit the user to insert a new contact into the collection 
#   of contacts. The program will prompt the user to enter the name of the new 
#   contact, prompt the user to enter the new contact's phone number, and 
#   prompt the user to enter the new contact's email address (three separate 
#   prompts, in the specified order); it will then insert the new contact into 
#   the dictionary of contacts.
#   This option will verify that the new contact's name is unique, that the 
#   phone number is formatted correctly (only digits, the character "-" in 
#   correct locations), and that the email address is formatted correctly (the
#   character "@" between the local part and the domain part).
#
#   Option D will permit the user to remove an existing contact from the 
#   collection of contacts. The program will prompt the user to enter the name 
#   of the contact; it will then remove that contact from the dictionary of 
#   contacts.
#
#   Option E will permit the user to replace the phone number for an existing 
#   contact.  The program will prompt the user to enter the name of an existing
#   contact, and then prompt the user to enter the replacement phone number.
#   This option will verify that the replacement phone number is formatted 
#   correctly.
#
#   Option F will permit the user to replace the email address for an existing 
#   contact.  The program will prompt the user to enter the name of an existing
#   contact, and then prompt the user to enter the replacement email address.
#   This option will verify that the replacement email address is formatted 
#   correctly.
#
#   Option G will permit the user to display a subset of the collection of 
#   contacts.  The program will prompt the user to enter a name prefix; the 
#   program will then display all information about each contact whose name 
#   begins with that name prefix.  That list of contacts will be displayed in 
#   sorted order, based on the contact names.
#   For example, if the name prefix is "Wi", then all contact names which begin
#   with the characters "Wi" will be displayed.
#   If the user enters an empty name prefix, all contacts in the collection 
#   will be displayed.
#
#   The program will detect, report and recover from invalid user inputs. 
#   Whenever the user enters an invalid input, the program will display an 
#   appropriate message on the screen and will then immediately return to the 
#   menu of options.  For example, assume the user selects option E (update 
#   existing #   contact's phone number), and then enters a contact name which
#   is not present in the dictionary.  The program will report the error to 
#   the user and will then prompt the user to select a menu option (it will not
#   re-prompt the user to enter a different contact name, it will not prompt 
#   the user to #   enter a phone number, and it will not modify the dictionary
#   of contacts).
###############################################################################
def name_test(name, dict_contact):
    """
    This function tests if the given name is already exist in dictionary.
    name: The name to test if it is in the dictionary (str)
    dict_contact: This is the dictionary to search name with (dictionary)
    Return: This function returns a boolean value.
    If the given name is already in the dictionary, return True.
    If the given name is not in the dictionary, return False.
    """
    # search if the name is in the dict_contact
    if name in dict_contact:
        return True
    else:
        return False

def tel_test(tel):
    """
    This fucntion tests if the phone number is formatted correctly.
    tel: This is the phone number to test.
    Return: This function will return boolean values.
    If the phone number formatted correctly, it will return True. Otherwise, it
    will return False.
    """
    # break the phone number into 3 sections and test if all section are number 
    # and are seperate by "-".
    if tel[0:3].isdigit() and tel[3] == "-" and tel[4:7].isdigit() and tel[7] \
    == "-" and tel[8:11].isdigit():
        return True
    else:
        return False

def email_test(email):
    """
    This function tests if the email is formatted correctly.
    email: This is the email address to test.
    Return: This fucntion will return boolean values.
    If the email address formatted correctly, it will return True. Otherwise, 
    it will return False.
    """
    is_valid = False    # initialize the return value as False.
    
    if email.count("@") == 1:   # one email address can only contain 1 "@"
        index_at = email.find("@") # get the index of "@"
        # seperate email address into two parts: local and domain.
        local = email[:index_at]
        domain = email[index_at+1:]
        # local should contain at least 1 character and domain should contain 
        # at least 3 characters.
        if len(local) > 0 and len(domain) > 2:
            # domain should contain a "." and "." should not be the first 
            # character and the last character in domain.
            if "." in domain and domain[0] != "." and domain[-1] != ".": 
                is_valid = True # if all true, set the return value as True.
    
    return is_valid

def opt_a():
    """
    This function will prompt user to enter a file name and read and store it 
    in a dictionary.
    Return: This function will return dict_contact which contain the 
    information from input file.
    """
    dict_contact = {} # initialize dict_contact
    try:
        # get the file name from user.
        file_name = input("Please enter the name of the input file:") 
        file_in = open(file_name, "r") # open the file.
        # loop to read file.
        for line in file_in:
            list_temp = line.split(";") # split line by ";"
            name = list_temp[0].strip() # get the name from list.
            tel = list_temp[1].strip()  # get the phone number from list.
            email = list_temp[2].strip()# get the email address from list.
            # store phone number and email address in a dictionary with the 
            # name as key.
            dict_contact[name] = [tel, email] 
        return dict_contact # return the dictionary
        file_in.close() # close the file
    # if file does not exist, return the error.
    except FileNotFoundError:
        print("File not exist!")

def opt_b(dict_contact):
    """
    This function write the dict_contact into the file specified by user.
    dict_contact: This is the dictionary to write into file.
    Retuen: This function do not return anything.
    """
    # get the name of output file from user.
    file_name = input("Please enter the name of the output file:") 
    file_out = open(file_name, "w") # open the file to write.
    list_out = [] # initialize the list to write in the file.
    # loop to read information from dict_contact
    for key, value in dict_contact.items():
        name = key          # get the name
        tel = value[0]      # get the phone number
        email = value[1]    # get the email address
        list_out.append([name, tel, email])# store information into output list.
        print(name, tel, email, sep=";", file=file_out) # write list into file.
    file_out.close() # close the file.

def opt_c(dict_contact):
    """
    This function will permit the user to insert a new contact into the 
    collection of contacts.
    dict_contact: This is the dictionary to add new contact into.
    Return: This function will return the new dict_contact.
    """
    # prompt user to enter the name
    name = input("Please enter the name:").strip()
    # call name_test function to check if name is already exist.
    if not name_test(name, dict_contact):
        # prompt user to enter the phone number.
        tel = input("Please enter the phone number:").strip()
        # call tel_test function to check if phone number is valid.
        if tel_test(tel): 
            # prompt user to input the email address.
            email = input("Please enter the email address:").strip()
            # call email_test function to check if the email address is valid.
            if email_test(email): 
                # add new contact into the dict_contact
                dict_contact[name] = [tel, email] 
            else:
                # if the email address is not valid, prompt user.
                print("Email address format error!") 
        else:
            # if the phone numebr is not valid, prompt user.
            print("Phone number format error!") 
    else:
        # if the name is already in the dict_contact, prompt user.
        print("Name already exist!") 
    return dict_contact # return the new dict_contact.

def opt_d(dict_contact):
    """
    This function will permit the user to remove an existing contact from the 
    collection of contacts.
    dict_contact: This is the dictionary to remove contact from.
    Return: This function will return the new dict_contact.
    """
    # prompt user to enter the name to remove.
    name = input("Please enter the name:") 
    if name_test(name, dict_contact): # check if the name is exist.
        dict_contact.pop(name) # remove the contact with the name if exist.
    else:
        print("Name not exist!") # prompt user if the name is not exist.
    return dict_contact # return the new dict_contact.

def opt_e(dict_contact):
    """
    This function will permit the user to replace the phone number for an 
    existing contact.
    dict_contact: This is the dictionary to replace the phone number with.
    Return: This function will return the new dict_contact.
    """
    # prompt user to enter the name to replece phone number.
    name = input("Please enter the name:") 
    if name_test(name, dict_contact): # check if the name is exist.
        # prompt user to enter the new phone number
        tel = input("Please enter the new phone number:") 
        if tel_test(tel): # test if the phone number is valid.
            # replace the old phone number to new phone number
            dict_contact[name][0] = tel 
        else:
            # prompt user if the phone number is not valid.
            print("Phone number format error!") 
    else:
        print("Name not exist!") # prompt user if the name is not exist.
    return dict_contact # return the new dict_contact.

def opt_f(dict_contact):
    """
    This function will permit the user to replace the email address for an 
    existing contact.
    dict_contact: This is the dictionary to replace the email address with.
    Return: This function will return the new dict_contact.
    """
    # prompt user to enter the name to replece email address
    name = input("Please enter the name:") 
    if name_test(name, dict_contact): # check if the name is exist.
        # prompt user to enter the new email address.
        email = input("Please enter the new email address:") 
        if email_test(email): # test if the email address is valid.
            # replace the old email address to new email address.
            dict_contact[name][1] = email 
        else:
            # prompt user if the email address is not valid.
            print("Email address format error!") 
    else:
        print("Name not exist!") # prompt user if the name is not exist.
    return dict_contact # return the new dict_contact.

def opt_g(dict_contact):
    """
    This function will permit the user to display a subset of the collection of
    contacts.
    dict_contact: This is the dictionary to display.
    Retuen: This function do not return anything.
    """
    # prompt user to enter the prefix to display
    prefix = input("Please enter the prefix:") 
    len_prefix = len(prefix) # get the length of prefix.
    list_out = [] # initialize the output list.
    # loop to read all information from dict_contact.
    for key in dict_contact.keys():
        if key[0:len_prefix] == prefix: # if the prefix found in the key value.
            name = key # get the name of this item
            tel = dict_contact[name][0] # get the phone number of this item
            email = dict_contact[name][1] # get the email address of this item
            list_out.append((name, tel, email))#store them into the output list
    list_out.sort() # sort the list by name.
    # print the list by element.
    for element in list_out:
        print(element[0], element[1], element[2], sep=";")

def opt_x():
    """
    This function display the exit information and do nothing.
    """
    print("Program Exited!")

def opt(dict_contact):
    """
    This function prompt user to enter the command and call the corresponding 
    function.
    dict_contact: the dictionary contain contact information to pass through 
    functions.
    """
    # prompt user to enter the command
    command = input("Please enter the command:")
    command = command.lower() # convert the inputed command to lower case.
    # call corresponding function by command.
    if command == "a":
        dict_contact = opt_a() # call corresponding function
        main(dict_contact) # return to the main function anyway
    elif command == "b":
        opt_b(dict_contact) # call corresponding function
        main(dict_contact) # return to the main function anyway
    elif command == "c":
        dict_contact = opt_c(dict_contact) # call corresponding function
        main(dict_contact) # return to the main function anyway
    elif command == "d":
        dict_contact = opt_d(dict_contact) # call corresponding function
        main(dict_contact) # return to the main function anyway
    elif command == "e":
        dict_contact = opt_e(dict_contact) # call corresponding function
        main(dict_contact) # return to the main function anyway
    elif command == "f":
        dict_contact = opt_f(dict_contact) # call corresponding function
        main(dict_contact) # return to the main function anyway
    elif command == "g":
        opt_g(dict_contact) # call corresponding function
        main(dict_contact) # return to the main function anyway
    elif command == "x":
        # call corresponding function to display exit information and do not 
        # retur ntoe main function to exit the program
        opt_x() 
    else:
        print("Command error!")#if user enter the invalid command, prompt user.
        main(dict_contact) # return to the main function anyway

def main(dict_contact):
    """
    This function display the command list and call opt function for next step.
    dict_contact: the dictionary contain contact information to pass through 
    functions.
    """
    print("A)  Read collection of contacts from file", \
    "B)  Write collection of contacts to file", \
    "C)  Add new contact", \
    "D)  Remove existing contact", \
    "E)  Update existing contact's phone number", \
    "F)  Update existing contact's email address", \
    "G)  Display contacts by prefix", \
    "X)  Exit from the program", sep="\n")
    opt(dict_contact) # call opt function for next step.

main({}) # call main function to run the program.