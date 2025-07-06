#write a list of comprehension that creates a new list of squares of even numbers from a given list
# using a lambda fucntion to check for even numbers

# 1. Get an input from users
# 2. using filter function get even numbers form list
# 3. using map function square those even numbers
# 4. store the square number in list and print the list

Numbers=(input("Enter the numbers"))
Numbers2=[int(i) for i in Numbers]
evennumbers=filter(lambda x: x%2==0,Numbers2)
squareof_numbers=map(lambda x:x*x,evennumbers)
print(list(squareof_numbers))

