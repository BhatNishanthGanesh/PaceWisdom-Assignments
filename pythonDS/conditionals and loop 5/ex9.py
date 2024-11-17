# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.


quantity = int(input("enter the quantity"))
cost = quantity*100

if cost>1000:
    final_cost = cost - (10/100)*cost
else:
    final_cost = cost

print(final_cost)        
