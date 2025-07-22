#sum of first n natural numbers 

#Recursion
def getSum(n):
    if n==1:
        return 1 
    return n+getSum(n-1)
n=10
print(getSum(n))


#Formula
n=10 
sum=(n*(n+1)/2) 
print(int(sum))


# for loop 
s=0
for i in range(n+1):
    s+=i 
print(s)
