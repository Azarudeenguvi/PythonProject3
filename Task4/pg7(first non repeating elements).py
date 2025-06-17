#In a list identify the first non repeatable item.
#create a loop to identify the repeating values.
#capture the first value and print

Newlist=[1,6,65,7552,2365,124,2365,5,124]
for i in Newlist:
    if Newlist.count(i)>1:
        print(i)
        break
else:
   print("There is no repeatable numbers")


