# Generate random number from the system
# Ask user to enter the guessed number
# check with conditions of user enter number matches with random number
# give more attempts until the correct number


# Approach 1 using for loop

import random
#
randomnumber=random.randrange(1,100)
Guessed_number=int(input("Enter the number from 1 to 100:-"))
for attempts in range(1,10):
      if randomnumber==Guessed_number:
        print("Awesome the number entered is correct")
        break
      elif randomnumber<Guessed_number:
         print("This is highest number")
      else:
         print("This is lowest number")
      Guessed_number = int(input("Enter the number from 1 to 100:-"))
else:
      print(f"Sorry, all your attempts are over- The correct number is {randomnumber}")


# Approach 2 using while loop

randomnumber=random.randrange(1,100)
Guessed_number=int(input("Enter the number from 1 to 100:-"))
attempt=1
while attempt<10:
    if randomnumber==Guessed_number:
        print("Coool, the guessed number is correct")
    elif randomnumber<Guessed_number:
        print("This is highest number")
    else:
        print("This is the lowest number")
    attempt += 1
    Guessed_number=int(input("Enter the number from 1 to 100:-"))
else:
  print(f"Sorry your attempts are over, the correct number is{randomnumber}")


