n=20

sum = 0
for i in range(1,n):
    if n%i==0:
        sum+=i 
if(sum>n):
    print(n , "is an Abundant Number") 
else:
    print(n , "is not an Abundant Number")