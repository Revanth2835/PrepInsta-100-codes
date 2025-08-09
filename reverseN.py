num = 1234

reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse) 

# n=1234 
# n_str = str(n) 
# reverse = n_str[::-1] 
# print(reverse)