
print( "\nWhen prompted, please enter an integer score" )
print( "(enter a negative score to terminate\n" )

# Initialize the current maxium to a value smaller than any valid score

maxm = -1

# Initialize the count to 1 (so prompt is "Enter score number 1: ")

num = 1

prompt = "Enter score number " + str(num) + ": "
score = int( input( prompt ) )

while score > 0:

    # If the score is greater than the current maximum score
    # then save the score as the current maximum score
    
    if score > maxm:
        maxm = score
    print( "  debug -- maximum score so far:", maxm )
    
    num += 1

    prompt = "Enter score number " + str(num) + ": "
    score = int( input( prompt ) )

print( "\nThe maximum score:", maxm )
print( "\nThe number of scores:", num - 1 )
