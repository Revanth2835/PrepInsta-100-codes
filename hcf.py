num1 = 36
num2 = 60
a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("Hcf of", a, "and", b, "is", num1) 

 Recursive function to return HCF of two number
def findHCF(num1, num2):
    
    # Everything divides 0
    if num1 == 0 or num2 == 0:
        return num1 + num2
    
    # base case
    if num1 == num2:
        return num1
    
    # num1>num2
    if num1 > num2:
        return findHCF(num1 - num2, num2)
    else:
        return findHCF(num1, num2 - num1)


num1 = 36
num2 = 60

print("Hcf of", num1, "and", num2, "is", findHCF(num1, num2))