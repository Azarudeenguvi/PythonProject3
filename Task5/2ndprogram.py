#Given a list of numbers, use the reduce function and lambda expression to calculate the product of all number is the list
from functools import reduce

# 1. Get a list of numbers from users
# 2. multiply all numbers from the list using reduce and print the product value.

usersinput=(input("Enter the numbers:-- "))
Eachnumber=[int(i)for i in usersinput]
product=reduce(lambda x,y:x*y,Eachnumber)
print(product)
