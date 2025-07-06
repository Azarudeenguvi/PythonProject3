# write a lambda function to check if the given string is a number

# 1. Get a users from input in string
# 2. using digit we can identify if string is a number or not
user_number=input("Enter the number:-- ")
number=lambda x:x.isdigit()

# ---->Here this print the true or false
print(number(user_number))