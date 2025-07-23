#sum of natural numbers in a given range

num1 ,num2 = 20, 30 
sum=0 
for j in range(num1,num2+1):
    sum+=j 
print("Sum of numbers from", num1, "to", num2, "is:", sum)