# def checkPalindrome(n):
#     for i in range(0,len(n)):
#         if n[i] != n[len(n)-i-1]:
#             return False 
#         return True
# n=input()  
# print("Palindrome") if checkPalindrome(n) else print("Not Palindrome")


# num=int(input())
# temp = num 
# reverse = 0
# while temp > 0:
#     digit = temp %10 
#     reverse = (reverse * 10) + digit 
#     temp =temp //10 

# if(num == reverse):
#     print("Palindrome") 
# else:
#     print("Not Palindrome")
    
    
    
n=input() 
print("palindrome") if (n==n[::-1]) else print("Not Palindrome")