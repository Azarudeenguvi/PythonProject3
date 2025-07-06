# Create a lambda fucntion to create a fibonocci series up to n terms
from functools import reduce

Number=[0,1]
n=int(input("Enter the number:-- "))
while len(Number)<n:
   list2=(lambda x,y:x+y)(Number[-1], Number[-2])
   Number.append(list2)
print(Number)
