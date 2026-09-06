import math

#Types of calculators avalibale for the user
print(
     "Investment - to calculate the amount of interest " 
     "you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

#Getting which calculator the user wants and defining parameters
name = input("Enter your name")
selected_financial_calculator = input(
    "Enter either investment or bond from the menu above to proceed:"
    ).lower()


#Investment calculator 
if selected_financial_calculator == "investment":
    principal_amount = float(input("How much money are you investing:"))
    expected_return = float(input("Interest rate:"))
    total_years= int(input("How many years do you plan on investing?"))
    type_of_interest = input("Compound interest or simple interest?").lower()

#Simple interest calculator  
    if type_of_interest in ["simple" or "simple interest"]:                                                                
        simpleinterest_return = principal_amount*(1+
        (expected_return/100)*total_years)
        print(f'Your expected return after {total_years} years is {simpleinterest_return}')
#Compound interest calculations
    elif type_of_interest in ["compound" or "compound interest"]:                
        compound_interest_return = principal_amount*math.pow(
        (1+expected_return/100),total_years)
        print(f'Hi,{name}! Your expected return after {total_years} years is {compound_interest_return}')
    else:
        print(f'Hi,{name}! You have entered the incorrect option, please try again')

#Return for bond payment
elif selected_financial_calculator == "bond":
    present_value = float(input("What is the present value of the house?"))
    interest_rate = float(input("Enter the interest rate:"))/100/12
    bond_repayment_months = int(input("Number of months"))
    repayments = (
    interest_rate *present_value)/(1 - (1+ 
    interest_rate)**(-bond_repayment_months))
    print(f'Hi,{name}! Your bond repayments after {bond_repayment_months} months is {repayments}') 
else:
    print("You have entered the incorrect option, please try again")
