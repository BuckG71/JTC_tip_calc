# function to validate tip input, need edge case if tip entered is < 0
def validate_tip_input(tip_input):
  is_float = False
  while is_float == False:
    try:
      float_tip_input = float(tip_input)
      is_float = True
      if float_tip_input < 0:
        print(input('Please enter a number greater than 0: '))
    except ValueError:
      print('You did not enter a decimal or integer, please try again: ')
    percentage = float_tip_input / 100
  return percentage

def validate_other_inputs():
  while True:
    user_input = input('(please enter a positive number greater than zero): ')
    try:
      int_value = float(user_input) 
      if int_value > 0:
        break
      else:
        print(f"Amount must be greater than zero, try again: ")
    except ValueError:
      print("Amount must be entered as digits only, try again: ")
  return int_value

def calc_total_bill(food, party_size, tip_pct):
  SALES_TAX_RATE = 0.1
  total_bill = food + (food * SALES_TAX_RATE) + (food * tip_pct)
  return total_bill 
