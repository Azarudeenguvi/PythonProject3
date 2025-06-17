sortlist=[62,58,14,23,18,9,120]
sortlist.sort()

# approach 1 using loop
for i in sortlist:
    print(i)
    break

#approach 2using index
print(sortlist[0])

Ratedlist=[10,8,6,5,2]
# Approach1
minimum=Ratedlist[0]
for i in Ratedlist:
    if i<minimum:
        minimum=i
print(i)

# Approach2
Minimum1=min(Ratedlist)
print(Minimum1)