n=int(input("Enter Number to check perfect square or not: "))

is_square =False 

for i in range(n+1) :
    if i*i ==n:
        is_square=True  
        break
    elif i*i > n:
        break 
    
if(is_square):
    print(n , "is a perfect square") 
else:
    print(n , "is NOT a perfect square")