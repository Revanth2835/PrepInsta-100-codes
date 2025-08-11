n=371 
num = n
sum=0 
digit =0 
length = len(str(n))
for i in range(len(str(n))):
    digit = int(num%10) 
    sum += pow(digit,length) 
    num = num//10 
if sum ==n:
    print("armstrong")
else:
    print("not armstrong")
    