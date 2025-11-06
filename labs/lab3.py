
#! 1 
# def div(a,b):
#     return a/b
# print(div(10,5))

#!  2
# def sq(num):
#     return num**2
# print(sq(4))  

#! 3
# nums=[5,2,4,5,6]
# print(f"max={max(nums)} min={min(nums)}")

#!4 


# def lower(name):
#     small=""
#     for i in name: #Anmol->anmol
#         if ord(i)>=65 and ord(i)<=90:
#             i=ord(i)+32
#             small+=chr(i)
#         else:
#             small+=i    
#     return small            

# username="AnmoL"


#? username=input("enter the username: ")
#? print(username.lower())

# num=int(input("Enter number to check it is negative positive or 0: "))
# func=lambda num:"positive" if num>0  else ("negative" if num<0 else "zero")
# print(func(num))


#? quiz 
#! How do you create a list of the first three elements from a list of lists using list comprehension?


# data = [[1, 2, 3, 4, 5], ["a", "b", "c", "d"], [10, 20, 30, 40, 50]]
# output=[elem[:3] for elem in data]
# print(output)

# print([str(i) + str(j) for i in range(3) for j in range(2)] )