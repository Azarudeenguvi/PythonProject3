# Ask user to enter the number
# Store the number in a variable
# Take 1st digit of that number and store in a new variable
# Tale last digit of that number and store is another new variable
# Add those 2numbers

Number=(input("Enter the number:-"))
Numberinlist=[Number]
separatethelist=list(Numberinlist[0])
firstdigit=(separatethelist[0])
original1=int(firstdigit)
lastdigit=(separatethelist[-1])
original2=int(lastdigit)
Sum=original1+original2
print(f"The sum of the first and last 2 digits are {Sum}")

