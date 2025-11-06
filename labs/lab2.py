
#! python program to check leap year
# year = int(input("Enter a year: "))
# if(year%4==0 and year%100 !=0):
#     print(f"{year} is a leap year")
# elif(year%100==0 and year%400==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


#!python program to find the largest among three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a>b and a>c:
#     print(f"{a} is largest")
# elif b>a and b>c:
#     print(f"{b} is largest")
# else:    
#     print(f"{c} is largest")


#! python program to check if a number is positive ,negative or 0
# number=int(input('enter number to get it is positive negative or zero: '))

# if number<0:
#     print(f"{number} is negative")
# elif number>0:    
#     print(f"{number} is positive")
# else:    
#     print(f"{number} is zero")



#!toy vendor supplies->battery based,key based,electrical charging based || battery based ->10% discount when 1000>
#! 5% key based if 100>
#! 10% electrical based if 500>
#!  (1,2,3) (b,k,e)

# product_code=int(input("Enter the product code  1 for battery based,2 for key based,3 for electrical charging based toy: "))

# if product_code not in (1,2,3):
#     print("product code is wrong enter the right code again: ")

# else:
#     amount=int(input("enter amount that you've been purchased the toy: "))
    
#     if product_code==1:
#         if amount>1000:
#             print(f"you buy battery based toy and your netAmount after 10% discount is {amount-amount*0.1}")
#         else:    
#             print(f"you buy battery based toy and your payable amount is {amount}")
#     elif product_code==2:
#         if amount>100:
#             print(f"you buy key based toy and your netAmount after 5% discount is {amount-amount*0.05}")
#         else:    
#             print(f"you buy key based toy and your payable amount is {amount}")
#     else:
#         if amount>500:
#             print(f"you buy electrical charging based toy and your netAmount after 10% discount is {amount-amount*0.1}")
#         else:    
#             print(f"you buy electrical charging based toy and your payable amount is {amount}")



# A transport company charges the fare acc to following table:


# distance      charges
# 1-50            8rs/km 
# 51-100          10rs/km
# >100            12rs/km