n=54
p=n 

sum=0 
while(p>0):
    sum= sum + (p%10) 
    p=p//10 
if(n%sum==0):
    print(n,"is a harshad number") 
else:
    print(n,"is not a harshad number")