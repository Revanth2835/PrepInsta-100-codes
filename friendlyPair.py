n,m= 6 , 234


sum_n =0
for i in range(1,n):
    if n%i==0:
        sum_n+=i  
        
        
sum_m =0
for j in range(1,m):
    if m%j==0:
        sum_m+=j 
        
if(sum_n%n == sum_m%m):
    print("Friendly Pair")
else:
    print("Not Friendly Pair")