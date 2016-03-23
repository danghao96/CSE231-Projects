############################################
#  Computer Project #1
#
#  input:
#  1. The distance to the finish line (in miles). 
#  2. The speed of the tortoise (in inches per minute). 
#  3. The speed of the hare (in miles per hour). 
#  4. The time that the hare rests after running (in minutes). 
#  5. The time that the hare runs before resting (in minutes).
#  output the times it takes both the tortoise and the hare to complete 
# the race.
#
############################################


dis = float (input ("How many miles will the tortoise and hare race? "))
# Input the distance to the finish line and convert it to float
speed_tort = float (input ("How many inches can the tortoise cover in one minute? "))
# Input the speed of the tortoise and convert it to float
speed_tort = speed_tort / 63360 * 60 
# Convert the speed of the tortoise to miles per hour

print("The tortoise takes", dis / speed_tort, "hours to finish the race.") 
# Calculate and print the time the tortoise needs to finish the race

speed_hare = float (input ("How many miles can the hare run in one hour? "))
# Input the speed of the hare and convert it to float
time_rests = float (input ("How long does the hare rest (in min)? "))
# Input the time the hare rests and convert it to float
time_runs = float (input ("How long does the hare run at a time (in min)? "))
# Input the time the hare runs and convert it to float

time_rests = time_rests / 60 # Convert time the hare rests from minute to hour
time_runs = time_runs/ 60 # Convert time the hare rests from minute to hour

time_totalrun = dis / speed_hare # Calculate the total time the hare runs
roun = time_totalrun // time_runs # Calculate the round the hare runs and rests
time_reminingrun = time_totalrun % time_runs 
# Calculate the time the hare runs besides the round
if time_totalrun % time_runs == 0: time_hare = roun * \
(time_runs + time_rests) - time_rests 
# When the race is finished as one run is finished
if time_totalrun % time_runs != 0: time_hare = roun * \
(time_runs + time_rests) + time_reminingrun 
# When the race is finished but one run is not finished

# Display the results with one digit after the decimal point
time_hare = float ((int (time_hare * 10)) / 10)

print("The hare takes", time_hare, "hours to finish the race.")
# Print the time the hare takes to finish the race