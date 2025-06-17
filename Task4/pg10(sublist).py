#provide list need to find if any sublist where sum is equal to 0

List=[4,2,-3,1,6]
SUM=0

for i in range(len(List)):
    for j in range(i+1,len(List)):
        for k in range(j+1,len(List)):
            if List[i]+List[j]+List[k]==SUM:
                sublist=[List[i],List[j],List[k]]
                print(f"The sublist values are {sublist}")