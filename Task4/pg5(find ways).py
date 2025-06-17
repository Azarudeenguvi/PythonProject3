#write a python program to find a ways to make 10 using Rs 1,2,5,10
#Make a list of those numbers
#iterate each number and multiply with each number in list

List=[1,2,5,10]
Amount=10
for i in range(len(List)):
    for j in range(i+1,len(List)):
        if List[i]*List[j]==Amount:
          Possible_ways=[List[i],List[j]    ]
          print(f"The possible ways are {Possible_ways}")
