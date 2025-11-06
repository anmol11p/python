
#! Write a decorator that prints "Before calling function" and "After calling function" around the execution of any function.

# def decorator(fx):
#     def fun(*args, **kwargs):
#         print('before calling function')
#         fx(*args,**kwargs)
#         print('after calling function')
#     return fun    

# @decorator
# def add(a,b):
#     print(a+b)
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# add(a,b)
# add=decorator(add) #pass the function
# print(add(a,b))


#! Decorator with Arguments
#! Create a decorator repeat(n) that runs the decorated function n times. 

# def decorator(fx):
#     def repeat(n):
#         for i in range(n):
#             print(i+1,"time")
#             fx()
#     return repeat
            
# # @decorator
# def hello():
#     print('helloworld')       
# hello=decorator(hello)  
# hello(3) 