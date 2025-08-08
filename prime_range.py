n=int(input())  
m=int(input())
# for i in range(n,m+1):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ") 
        
        
        
for i in range(n, m + 1): 
    p = []
    flag=0
    if i > 2:
        continue 
    if i ==2:
        p.append(i) 
    for x in range(2,i):
        if i%x ==0:
            flag =1 
            break 
    if flag ==0:
        p.append(i) 
print(p)