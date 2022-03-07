# import functions
from tip_calc_functions import *

# user greeting
print('\nThank you for choosing Bryan\'s Tip-Top Tip Calculator!')

# USER INSTRUCTIONS
print('\nINSTRUCTIONS')
print('You will be prompted to enter total food cost, number of people in your party, and the desired tip percentage.')
print('The app will use your inputs to calculate the total bill, including tax and tip, and the amount each person in your party should pay.')
input('Press enter when ready to start.')

# INPUT SECTION
# call input validation functions to get user inputs in proper format (i.e. - integer or float)
print('\nUSER INPUTS')
print('Total food costs')
food_cost = validate_other_inputs()
print('\nNumber of people splitting the bill')
people_in_party = validate_other_inputs()
# tip percentage validated separately to allow user to enter 0, and to convert input to decimal percentage
tip_percentage = validate_tip_input(input('\nWhat percentage do you wish to tip? (Note: 0.5 = 0.5%, not 50%) '))

# MATH
# calculate total bill, including tax and tip
total_bill = calc_total_bill(food_cost, people_in_party, tip_percentage)
# use f string to format as currency
formatted_total_bill = "${:,.2f}".format(total_bill)

# calculate each person's share
# able to use f string to format as currency within variable declaration as no further calculations are done using this variable
per_person = "${:,.2f}".format(total_bill / people_in_party)

# OUTPUT SECTION
# output total bill and per-person share, both formatted as currency
print(f'\nThe total bill for your party is: {formatted_total_bill}')
print(f'Each person should pay: {per_person}\n')