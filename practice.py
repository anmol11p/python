
#! Write a Python program that:
# Takes two numbers as input.
# Calculates their sum, difference, product, quotient, and remainder.
# Prints the results.

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# sum=a+b 
# difference=a-b
# product=a*b 
# quotient=a/b 
# remainder=a%b 

# print(sum,difference,product,quotient,remainder)

#! Write a Python program that:
# Takes a number as input.
# Checks if the number is positive, negative, or zero.
# Prints the result.

# number=int(input("Enter  number: "))

# if(number>0):
#     print(number," is positive")

# elif(number<0):
#     print(number," is negative")

# else:
#     print(number," is Zero")


#! Prints all even numbers from 1 to 20.
# for i in range(1,21):
#     if i%2 == 0:
#         print(i) 
#         continue    

#! Write a Python function is_prime(n) that:
# Takes a number n as input.
# Returns True if the number is prime, False otherwise. 

# def isPrime(n=5):
#     if n<=1:
#         print(f"{n} is not a valid number to check.")
#     else:
#         i=2
#         is_Prime=True
#         while(i*i<=n):
#             if n%i==0:
#                 i+=1
#                 is_Prime=False
#                 break
#             i+=1
#         print(f"{n} is prime number") if is_Prime else print(f'{n} is not a prime')    
# n =int(input("Enter a number: "))
# isPrime(n)

#! Write a Python program that:
#! Takes a list of numbers from the user (comma separated).
#! Finds the maximum and minimum numbers in the list.
#! Prints the results. 
# def maxElement(numbers):
#     max=numbers[0]
#     for i in range(1,len(numbers)):
#         if numbers[i]>max:
#             max=numbers[i]
#     return max

# by recursion 
# def maxElement(numbers,length):
#     if length==1:
#         return numbers[0]
#     max=maxElement(numbers,length-1)
#     if(max>numbers[length-1]):
#         return max
#     else:
#         return numbers[length-1]            

# def minElement(numbers):
#     min=numbers[0]
#     for i in range(1,len(numbers)):
#         if numbers[i]<min:
#             min=numbers[i]
#     return min



# numbers=list(map(int,input("Enter numbers maintain space between each element: ").split()))
# print(maxElement(numbers,len(numbers)))
# print(minElement(numbers))


#! Write a Python program that:
#! Takes a string as input.
#! Counts how many vowels (a, e, i, o, u) are in the string.
#! Prints the total vowel count. 

# def countVowel(user_Input):
#     count=0
#     vowels="aeiouAEIOU"
#     for i in range(0,len(user_Input)):
#         for j in range(0,len(vowels)):
#             if user_Input[i]==vowels[j]:
#                 count+=1
#                 break
#     return count            


# user_Input=input("Enter something.. to count vowel in it ")
# print(countVowel(user_Input))
