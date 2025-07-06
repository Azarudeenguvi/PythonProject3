#Given a list of dictionaries, each representing a person with 'name' and 'age' keys use lambda fucntions
# to filter out people under 18 and then map the remaining peoples names to a new list

persons=[{'Name':'Azarudeen','Age':'18'},{'Name':'sathish','Age':'21'},{'Name':'Remo', 'Age':'15'},{'Name':'master', 'Age':'22'}]
Age1=filter(lambda x:int (x['Age'])>=18,persons)
person1=map(lambda x:x['Name'],Age1)
print(list(person1))
