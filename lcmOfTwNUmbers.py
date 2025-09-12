n,m = 18,36 

greatest = max(n,m) 
lcm=0

while True:
    if(greatest % n ==0 and greatest %m ==0):
        lcm = greatest 
        break
    greatest += 1 
    
print(lcm)