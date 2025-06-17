# You have given a python list [10,501,22,37,100,999,87,351] your task is to count all the prime numbers
# Create a new python list which will contain all prime numbers in it

Numbers=[10,501,22,37,100,999,87,351]
primes= []
for i in Numbers:
    if i>1:
        for j in range(2,i):
            if i%j==0:
               break
        else:
            primes.append(i)
print(len(primes))
print(primes)





