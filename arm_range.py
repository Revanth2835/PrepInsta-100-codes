low=int(input()) 
high =int(input())

for n in range(low,high+1):
    sum=0
    temp=n
    order =len(str(n)) 
    while temp > 0:
        digit =temp %10 
        sum+=digit**order 
        temp //=10 
    if n==sum:
        print(n,end=', ')
