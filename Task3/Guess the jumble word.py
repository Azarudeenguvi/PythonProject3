#Pick any words from the list
#convert that word to list
#convert that list to letters
#jumber those letters
#convert those letters to jumbled word
#send to user and ask user to enter the correct word
import random

words=['python','javascript','Java','automation','pytest','guvi','selenium']

#Approach 1 using while loop

chooseword=random.choice(words)#-->pick of word from list
# print(chooseword)
list1=[chooseword]#---> convert this to list
# print(list1)
letter=list(list1[0])#--->convert this words to letters in list
# print(letter)
random.shuffle(letter)#--->shuffle the letters
# print(letter)
lettertoword=''.join(letter)#--->join those letters as word
print(lettertoword)
attempt=1
while attempt<=4:
    Guessedword=(input("Enter the correct word:--"))
    if chooseword==Guessedword:
        print("Hurray, you found the correct word")
        break
    else:
        print("Sorry, try again")
        attempt+=1
else:
   print("Sorry your turn is completed")






