from math import acos

i = int(input("Enter the number of decimals to calculate to:"))
pi = round(2 * acos(0.0), i)
print("Value of pi till the", i ,"th digit: ", pi)
