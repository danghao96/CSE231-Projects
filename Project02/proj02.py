##############################################################################
#  Computer Project #2
#
#  This Python program is for analyzing the Gaussian distribution 
#  algorithm implemented by the gauss function in the random module.
#
#  Algorithm
#    prompt for the desired mean μ in float
#    prompt for the desired standard deviation σ in float
#    prompt for the number of values num that are to be generated in int
#    
#    The program will call function gauss with the user-supplied mean and 
#    standard deviation a total of num times.
#
#    Call gauss function and compute:
#    a.  The range of the generated values.
#    b.  The actual mean (i.e., the average) of the generated values.
#    c.  The percentages of the generated values that are:
#        1 -- more than two standard deviations above the desired mean
#        2 -- above and within two standard deviations of the desired mean
#        3 -- above and within one standard deviation of the desired mean
#        4 -- at the desired mean (within 1.0e-6 of the desired mean)
#        5 -- below and within one standard deviation of the desired mean
#        6 -- below and within two standard deviations of the desired mean
#        7 -- more than two standard deviations below the desired mean
#    
#    output followw:
#        a. A brief description of what the program does.
#        b. A synopsis of the inputs that it received. Floating point inputs 
#        will be rounded to two decimal places of accuracy when displayed.
#        c. The results of the analyses, appropriately labeled and in the 
#        order listed above. Values indicating the range and average will be 
#        rounded to two decimal places of accuracy when displayed. Percentages 
#        will be rounded to whole numbers and displayed without any decimal 
#        point.
#
##############################################################################



import random
random.seed( 0 )
print ("This program analyzes Python's Gaussian distribution algorithm.")

# Prompt the user for two float numbers and one int number

DES_MEAN_STR = input ("Enter the desired mean: ")
DES_DEVIATION_STR = input ("Enter the desired standard deviation: ")
NUM_STR = input ("Enter the number of values to generate: ")

# Convert the user inputs into float and int values

DES_MEAN = float ( DES_MEAN_STR )
DES_DEVIATION = float( DES_DEVIATION_STR )
NUM = int ( NUM_STR )

# create and initial all variables

act_mean = 0
s_value = DES_MEAN
l_value = DES_MEAN
higher_than_2_standard_deviations = 0
higher_than_1_standard_deviation = 0
higher_than_mean = 0
equalto_mean = 0
lower_than_mean = 0
lower_than_1_standard_deviation = 0
lower_than_2_standard_deviations = 0

# generate the gauss random numbers one by one and analysz these numbers

for value in range (NUM):
    
    dist = random.gauss ( DES_MEAN, DES_DEVIATION ) # generate gauss random 
    # numbers
    act_mean = act_mean + dist # add all the generated numbers to calculate 
    # the actual mean value
    
    # looking for the smallest number
    if s_value > dist:
        s_value = dist
    
    # looking for the largest number
    if l_value < dist:
        l_value = dist
        
# calculate the percentages of the generated values that are :
#        1 -- more than two standard deviations above the desired mean
#        2 -- above and within two standard deviations of the desired mean
#        3 -- above and within one standard deviation of the desired mean
#        4 -- at the desired mean (within 1.0e-6 of the desired mean)
#        5 -- below and within one standard deviation of the desired mean
#        6 -- below and within two standard deviations of the desired mean
#        7 -- more than two standard deviations below the desired mean
    if dist > DES_MEAN + 2 * DES_DEVIATION:
        higher_than_2_standard_deviations += 1
    elif dist > DES_MEAN + DES_DEVIATION:
        higher_than_1_standard_deviation += 1
    elif dist > DES_MEAN:
        higher_than_mean += 1
    elif dist == DES_MEAN:
        equalto_mean += 1
    elif dist < DES_MEAN - 2 * DES_DEVIATION:
        lower_than_2_standard_deviations += 1
    elif dist < DES_MEAN - DES_DEVIATION:
        lower_than_1_standard_deviation += 1
    elif dist < DES_MEAN:
        lower_than_mean += 1

act_mean = act_mean / NUM # calculate the actual mean value

# convert the percentage values to 2 digit integers

percent_higher_than_2_standard_deviations = \
int ( 100 * float ( higher_than_2_standard_deviations / NUM ) )
percent_higher_than_1_standard_deviation = \
int ( 100 * float ( higher_than_1_standard_deviation / NUM ) )
percent_higher_than_mean = int ( 100 * float ( higher_than_mean / NUM ) )
percent_equalto_mean = int ( 100 * float ( equalto_mean / NUM ) )
percent_lower_than_mean = int ( 100 * float ( lower_than_mean / NUM ) )
percent_lower_than_1_standard_deviation = \
int ( 100 * float ( lower_than_1_standard_deviation / NUM ) )
percent_lower_than_2_standard_deviations = \
int ( 100 * float ( lower_than_2_standard_deviations / NUM ) )

# convert all other values to float with two decimal points

DES_MEAN_2 = round( DES_MEAN, 2 )
DES_DEVIATION_2 = round( DES_DEVIATION, 2 )
s_value_2 = round(s_value, 2)
l_value_2 = round(l_value, 2)
act_mean_2 = round(act_mean, 2)

# print all the results

print ()
print ("The requested mean: ", DES_MEAN_2 )
print ("The requested standard deviation: ", DES_DEVIATION_2 )
print ("The number of values generated: ", NUM )
print ()
print ("The values ranged from", s_value_2, "to", l_value_2 )
print ("The actual mean was", act_mean_2 )
print ()
print ("The values distributed as follows:")
print ("  ", percent_higher_than_2_standard_deviations, "percent were higher \
than the mean by more than two standard deviations")
print ("  ", percent_higher_than_1_standard_deviation, "percent were higher \
than the mean and within two standard deviations")
print ("  ", percent_higher_than_mean, "percent were higher than the mean and \
within one standard deviation")
print ("  ", percent_equalto_mean, "percent were at the mean")
print ("  ", percent_lower_than_mean, "percent were lower than the mean and \
within one standard deviation")
print ("  ", percent_lower_than_1_standard_deviation, "percent were lower \
than the mean and within two standard deviations")
print ("  ", percent_lower_than_2_standard_deviations, "percent were lower \
than the mean by more than two standard deviations")