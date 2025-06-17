List=[10,20,30,9]
Value=59
for i in range(len(List)):
    for j in range(i+1,len(List)):
        for k in range(j+1,len(List)):
            if List[i]+List[j]+List[k]==Value:
                triplelist=[List[i],List[j],List[k]]
print(f"Ths sum of the 3 numbers from lists are {triplelist}")
