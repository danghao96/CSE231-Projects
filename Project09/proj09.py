import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
        of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    '''
    That function has no parameters.  It creates and initializes the stock, 
    tableau, and foundation, and then returns them as a tuple, in that order.
    Return a tuple (stock, tableau, foundation) for a new game, where
       - stock is a shuffled deck minus the 4 cards dealt to the tableau 
       - foundation is an empty list
       - tableau is a list of lists, each containing one of the dealt cards
    '''
    # call cards class Deck function to initialize the sotck
    stock = cards.Deck()
    stock.shuffle() # call shuffle function to shuffle the stock
    
    # initialize the lists
    foundation = []
    tableau1 = []
    tableau2 = []
    tableau3 = []
    tableau4 = []
    
    # deal the card and initialize the tableau
    tableau1.append( stock.deal() )
    tableau2.append( stock.deal() )
    tableau3.append( stock.deal() )
    tableau4.append( stock.deal() )
    
    # store tableaus in the list tableau
    tableau = [tableau1, tableau2, tableau3, tableau4]
    
    return (stock, tableau, foundation)  
    
def deal_to_tableau( stock, tableau ):
    '''Deal a card from the stock to each column of the tableau.'''
    """
    It will deal a card from the stock to each column of the tableau, unless 
    the stock has fewer than 4 cards; in which case it will just deal a card 
    to consecutive columns until the stock is empty.
    stock( list ): the data structure representing the stock 
    tableau( list ): the data structure representing the tableau. 
    """
    # if statement to judge if the stock has enough cards.
    if len(stock) > 4: # if it has enough cards, deal the card to each tableau
        for i in range( 4 ):
            tableau[i].append( stock.deal() )
    else:#if it doesn't have enough cards, deal the card to tableau in sequence
        for i in range( len( stock ) ):
            tableau[i].append( stock.deal() )

def display( stock, tableau, foundation ):
    '''Display the stock, tableau, and foundation.'''
    """
    A header line will be displayed labeling the stock, tableau, and foundation.
    Under the “stock” header, a non-empty stock will be displayed as “XX”, and 
    an empty one will be displayed as whitespace.
    Under the “tableau” header, each column of the tableau will be displayed in
    order: a non-empty column by the cards in the column, in order, from the 
    first card moved that is still left in the column (top) to the last card 
    moved that is still left in the column (bottom); and an empty column will 
    be displayed by whitespace.
    Under the “foundation” header, a non-empty foundation will be displayed as 
    the top card in the foundation (i.e. last card moved to it); and an empty 
    foundation will be displayed as whitespace.

    stock( list ): the data structure representing the stock.
    tableau( list ):  the data structure representing the tableau.
    foundation( list ): the data structure representing the foundation.
    """
    print()
    print("stock      tableau     foundation")
    
    # judge if stock is empty for display
    if len( stock ) > 0:
        stock_display = " XX    "
    else:
        stock_display = "       "
    
    line_num = 0 # initialize the number of lines to display
    for i in range( 4 ):
        if len( tableau[i] ) > line_num:
            line_num = len( tableau[i] )
    
    # for loop to display
    for i in range( line_num ):
        
        # if it is the first line, display the stock state and foundation
        if i == 0:
            print( stock_display, end="" ) # display the stock state
            # for loop to display the tableau for the first line
            for j in range( 4 ):
                # judge if the tableau is empty
                # if it's not empty, display the card in it
                if len( tableau[j] ) >= i+1: 
                    print( str( tableau[j][i] ).center( 4 ), end="" )
                else: # if it's empty, display space.
                    print( "    ", end="" )
            # if foundation is not empty, display last card in it.
            if len( foundation ) > 0:
                print( str( foundation[-1] ).rjust( 7 ) )
            else:
                print()
        
        # if it's not the first line, only display the tableau
        else:
            print( "       ", end="" ) # display blank replace the stock state
            # for loop to display the tableau for the first line
            for j in range( 4 ):
                # judge if the tableau is empty
                # if it's not empty, display the card in it
                if len( tableau[j] ) >= i+1:
                    print( str( tableau[j][i] ).center( 4 ), end="" )
                else: # if it's empty, display space.
                    print( "    ", end="" )
            print()
    

def get_option():
    '''Prompt the user for an option and check that the input has the 
       form requested in the menu, printing an error message, if not.
       Return:
       - empty list, if the input is not of the requested form
       - ['D'], for Deal
       - ['F', x], for move to foundation, where x is the (int) tableau index 
            of the specified column number 
       - ['T', x, y], for move within the tableau, where x and y are the (int)
            tableau indices of the specified column numbers
       - ['R'], for restart
       - ['H'], for displaying the menu
       - ['Q'], for quit
    '''
    option = input( "Input an option (DFTRHQ): " ) # get the option
    try:
        # strip, upper the input and store if in a list
        option_out = option.strip().upper().split()
        # if the input option is "D" or "R" or "H" or "Q", directly output the list
        if (option_out[0] == "D" or option_out[0] == "R" or option_out[0] == "H" \
        or option_out[0] == "Q") and len( option_out ) == 1:
            option_out = option_out
        # if the option if "F x", change the x in int and store in a list.
        elif option_out[0] == "F" and len( option_out ) == 2:
            try:
                if 0 < int( option_out[1] ) < 5:
                    option_out[1] = int(option_out[1]) - 1
                else: # if x's value is not from 1 to 4, output the error
                    option_out = "Error in option: " + option
            except ValueError: # if x is not an int, optput the error.
                option_out = "Error in option: " + option
        # if the option if "T x y", change the x in int and store in a list.
        elif option_out[0] == "T" and len( option_out ) == 3:
            try:
                if 0 < int( option_out[1] ) < 5 and 0 < int( option_out[2] ) < 5:
                    option_out[1] = int( option_out[1] ) - 1
                    option_out[2] = int( option_out[2] ) - 1
                else: # if x's or y's values are not from 1 to 4, output the error
                    option_out = "Error in option: " + option
            except ValueError: # if x or y is not an int, optput the error.
                option_out = "Error in option: " + option
        # if the input is not specified, output the error
        else:
            option_out = "Error in option: " + option
    except IndexError: # if user input empty string, return error message
        option_out = "Error in option: " + option

    return option_out
            
def validate_move_to_foundation( tableau, from_col ):
    '''Return True if the rules allow the bottom card in the tableau column  
       specified by from_col to be moved to the foundation; False, otherwise.
       If the move is invalid, print an appropriate error message.
    '''
    """
    tableau( list ):  the data structure representing the tableau.
    from_col( int ):  the column whose bottom card should be moved.
    """
    # A card can be moved to the foundation only if a higher ranked card 
    # of the same suit is at the bottom of a Tableau column.
    
    validate = False # initialize the output value as false
    # if the selected tableau have at least one card, take if as card_selected
    if len( tableau[from_col] ) > 0:
        card_selected = tableau[from_col][-1]
    
    # for loop to compare the selected card with the all four cards.
    for i in range (4):
        # only compare with those tableau with at least 1 card
        if len( tableau[from_col] ) > 0 and len( tableau[i] ) > 0: 
            # judge if the suit are same before compare the rank
            if tableau[i][-1].suit() == card_selected.suit():
                # get the rank from card in tableau
                rank_tableau = tableau[i][-1].rank()
                # get the rank from card selected
                rack_card = card_selected.rank()
                # take Ace as the highest rank.
                if rank_tableau == 1:
                    rank_tableau = 100
                if rack_card == 1:
                    rack_card = 100
                # only if the rank of card in tableau larger than the rank of 
                # card selected, change the output value to true.
                if rank_tableau > rack_card:
                    validate = True
        
    return validate


def move_to_foundation( tableau, foundation, from_col ):
    '''If valid, move a card from the tableau column specified by from_col to 
       the foundation.
    '''
    """
    tableau( list ):  the data structure representing the tableau.
    foundation( list ): the data structure representing the foundation.
    from_col( int ):  the column whose bottom card should be moved.
    """
    # check the validate
    if validate_move_to_foundation( tableau, from_col ):
        # append selected card to foundation
        foundation.append( tableau[from_col][-1] ) 
        tableau[from_col].pop( -1 ) # delete the card from tableau
        

def validate_move_within_tableau( tableau, from_col, to_col ):
    '''Return True if the rules allow the bottom card in the tableau column  
       specified by from_col to be moved to the tableau column specified by
       to_col; False, otherwise.
       If the move is invalid, print an appropriate error message.
    '''
    """
    tableau( list ):  the data structure representing the tableau.
    from_col( int ):  the column whose bottom card should be moved.
    to_col( int ):  the column the card should be moved to.
    """
    
    validate = False # initialize the output value as false
    # if the tableau whose card should be moved has at least 1 card and the 
    # tableau the card should be moved to has zero card, vhange the output
    # value as true
    if len( tableau[from_col] ) > 0 and len( tableau[to_col] ) == 0:
        validate = True
    
    return validate  

def move_within_tableau( tableau, from_col, to_col ):
    '''If valid, move a card from the tableau column specified by from_col 
       to the tableau column specified by to_col. 
    '''
    """
    tableau( list ):  the data structure representing the tableau.
    from_col( int ):  the column whose bottom card should be moved.
    to_col( int ):  the column the card should be moved to.
    """
    # check the validate
    if validate_move_within_tableau( tableau, from_col, to_col ):
        # append selected card to the column the card should be moved to.
        tableau[to_col].append( tableau[from_col][-1] )
        tableau[from_col].pop( -1 ) # delete the card from tableau

        
def check_for_win( stock, tableau ):
    '''Return True if the game is won: the only cards left in the tableau are
       the 4 aces and the stock is empty.  Otherwise, return False
    '''
    """
    stock( list ): the data structure representing the stock.
    tableau( list ):  the data structure representing the tableau.
    """
    # initialize the boolean variables
    is_clear = False
    is_all_A = True
    is_win = False
    
    # if the length of stock is 0, set the is_clear as true
    if len( stock ) == 0:
        is_clear = True
    
    # for loop to check if the cards in the tableau are all ace
    for i in range( 4 ):
        for card in tableau[i]:
            if card.rank() != 1:
                # if one of the card is not ace, change the is_all_A to False
                is_all_A = False 
    # if both variable are True, change the return value is_win to true
    if is_all_A and is_clear:
        is_win = True
    
    return is_win 

print( RULES ) # print the Rule

# call init_game function to initialize the game
stock, tableau, foundation = init_game() 

print( MENU ) # print the manu
display( stock, tableau, foundation ) # display the initial state of game

# main loop to run the program
while True:
    option = get_option() # get user's option for each loop
    # if statement to judge the input option
    # if option is "D", call function to deal to tableau
    if option[0] == "D":
        deal_to_tableau( stock, tableau )
        
        # check if user wins at the end of each round.
        if check_for_win( stock, tableau ):
            print( "You Win!" )
            break # if user wins, break the program.
        else:
            display( stock, tableau, foundation) # display the current state
    # if option is "F", call function to check validate and try move the card

    elif option[0] == "F":
        from_col = option[1]
        if validate_move_to_foundation( tableau, from_col ):
            move_to_foundation( tableau, foundation, from_col )
        # check if user wins at the end of each round.
        if check_for_win( stock, tableau ):
            print( "You Win!" )
            break # if user wins, break the program.
        else:
            display( stock, tableau, foundation) # display the current state
    # if option is "T", call function to check validate and try move the card

    elif option[0] == "T":
        from_col = option[1]
        to_col = option[2]
        if validate_move_within_tableau( tableau, from_col, to_col ):
            move_within_tableau( tableau, from_col, to_col )
        display( stock, tableau, foundation) # display the current state
    # if option is "R", restart the game

    elif option[0] == "R":
        stock, tableau, foundation = init_game() # initialize the game
        print( "=========== Restarting: new game ============" ) #print restart
        print( MENU ) # print manu
        display( stock, tableau, foundation ) # display the current state
        continue # jump the the beginning of the loop
    # if option is "R", diaplay the manu and the current state

    elif option[0] == "H":
        print( MENU ) # display the manu
        display( stock, tableau, foundation ) # display the current state
    # if option is "Q", quit the game and display the quit message

    elif option[0] == "Q":
        print( "You have chosen to quit." ) # display the quit message
        break # break the loop to exit the program
    # print error message generated by get_option function

    else:
        print( option ) # print the error message
    
    # check if user wins at the end of each round.
    if check_for_win( stock, tableau ):
        print( "You Win!" )
        break # if user wins, break the program.