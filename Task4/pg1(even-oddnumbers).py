# You have given a python list [10,501,22,37,100,999,87,351] your task is to create two lists
# List one which have all even numbers and another list which will have all th odd numbers in it

Numbers=[10,501,22,37,100,999,87,351]
Even =[]
odd=[]
for i in Numbers:
    if i%2==0:
        Even.append(i)
    elif i%2!=0:
        odd.append(i)
print(Even)
print(odd)




