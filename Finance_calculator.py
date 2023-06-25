#import math

print("Investment - to calculate the amount of interest you'll earn on your investment \n \n Bond - to calculate the amount you'll have to pay on a home loan \n")

investment_or_bond = (input("Enter either investment or bond from the menu above to proceed: ")).capitalize()




if investment_or_bond == "Investment":
    P = int(input("Enter deposit amount here: £"))
    r = int(input("Enter interest rate here: %"))/100
    t = int(input("Enter length of period in years here: "))
    SI_CI = (input("Simple or compound interest? : ")).capitalize()
    if SI_CI == "Simple":
         A = P*(1 + r*t)
         print("You will receive £" + str(A) + ".")
    else:
         A = P * pow((1+r),t)
         print("You will receive £" + str(A) + ".")
         
elif investment_or_bond == "Bond":
     P = int(input("present value of the house: £"))
     i = int(input("interest rate, e.g 6 : "))/1200 # 
     n = int(input("enter length of period to repay bonds in months, e.g 120 (10yrs): "))
     repayment = (i * P)/(1 - (1 + i)**(-n))
     print(repayment)
else:
     print("Please make sure bond or investment is spelt properly")


     