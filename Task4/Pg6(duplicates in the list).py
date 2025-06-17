#Combile all those lists in single list
#FInd a count of each value
#If count more than 2 store as separate list

List1=[20,10,20.99,True,'azar','mohamed']
List2=[10,'Man','women',True,]
List3=['Man',20.99,'third',3,'azar']
List1.extend(List2)
List1.extend(List3)
duplicate=[]
for i in List1:
    if List1.count(i)>1:
        duplicate.append(i)
    else:
        print(f"Thest values are not repeatable {i}")
print(duplicate)