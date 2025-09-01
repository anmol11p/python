# count =10
# def increment():
#     global count
#     count+=1
#     print(count)

# print(count) #10
# increment() #11
# print(count) #11



# def outer():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         print(count)
#     inner() #1
#     inner() #2  
# outer() 


class college():
    collegename="Jb knowledge park"
    def __init__(self,name,age):
        self.name=name  #instance variable
        self.age=age    #instance variable  

student1=college("anmol",23)
student2=college("anubhav",21)

# print(student1.name,student1.age)
# print(student1.collegename)


# ============== day 2 ==============


class student():
    species="Human"
    def __init__(self,name,age):
        self.name=name
        self.age=age

anmol=student("Anmol",23)
# print(anmol.name)
# print(anmol.species)

# single quote/double quote
# triple quote
''' 
aaaaaaa
'''

''' aaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaa
aaaaaaaaa '''


# list(mutable)

fruits=["apple",'banana','orange']
fruits[0]='seb'
# print(fruits)

# tuple(immutable)
fruits2=("apple",'banana','orange')
# fruits2[0]='seb' # line nt executed
# print(fruits2) #TypeError: 'tuple' object does not support item assignment


# set (mutable)
set_1={1,2,3,1,2}
# print(set_1) # {1, 2, 3}


# frozenSet (immutable=unchangeable)

froze=frozenset([1,2,3,4,4,5,6,5,9])
# print(froze)


#            ======= day-3 =====


# dictionary
new_dict ={"name":"Anmol","Age":28
}
#            ======= day-4 =====
# new_dict['name']="Anubhav"
# print(new_dict) #it is mutable
# print(new_dict['name'])


# type cast krna hai implicit or explicit
# process of convering one datatype to another datatype
# 1) implicit
# x=10
# y=5.5
# z=x+y
# print(type(z)) #automatically float the data
# 2)explicit

# int
# float 
# str
# list
# tuple
# set

# ===== string to int ========
# age=int("28")
# or
# age1="25"
# new_age=int(age1)
# print(type(age))

# ======== int to string =======
# age=28
# newAge=str(age)
# print(type(newAge))

# ======= list to set============
# arr=[1,2,3,4,5,6,1,5,6]
# converted_set=set(arr)
# print(converted_set)

# ============string to float============

# string_value="3.14"
# float_value=float(string_value)
# print(type (float_value))



#  ======== tuple to list =====
# x=(10,20)
# y=list(x)
# print(type(y))

# =========operators=============
# Arithmetic Operators:
# + - / * %  **  //
# 7 // 2 results in 3, because 7 divided by 2 is 3.5, and floor division rounds down to 3.

# Assignment Operators:
# = += -= /= *=  %= **=  //=

# Comparison (Relational) Operators:
# ==  != > >= < <=

# Logical Operators:
# and (Logical AND)
# or (Logical OR)
# not (Logical NOT)

# bitwise operators

# print(5&3) #and
# print(5|3) #or
# print(~5)  #not symbol=tilde,0s become 1s, and 1s become 0s.
# print(5^3) #xor
# print(5>>1) #right sift
# print(5<<1) #left shift
'''
Identity Operators:
Used to compare the memory locations of two objects.
is (Returns True if both variables point to the same object)
is not (Returns True if both variables do not point to the same object)
example 
a=[1,2,3]
x=a
print(a is x) #true
'''

'''
Membership Operators:
Used to test if a sequence contains a specific value.
in (Returns True if a value is found in the sequence)
not in (Returns True if a value is not found in the sequence)

# generally array wagerah me use hota hai
# for (i in arr)
example 
a=[1,2,3]
print(1 in a) #true
'''

# ========= day-5 ===========

# input function

# name=input("Enter your name:")
# age=int(input("Enter your age: ")) #by default it takes string as input
# print(f"your name is {name} and age is {age} ")


# a = list(map(int,input("Enter three numbers: ").split()))

# sum=0
# for i in a:
#     sum+=i

# print(f"addition of your numbers is: {sum}")    

'''
numbers=[]
for i in range(3):
    a=int(input(f"enter {i+1} number: "))
    numbers.append(a)

print(numbers)    
print (f"the sum of 1,2,3 is {1+2+3}")
'''

# some print things

# print("Hello",end=" to ")
# print("World")


'''
common_string= "Your grade is"
marks=int(input("Enter marks to check grade: "))
if(marks>=90):
    print(f'{common_string} A')

elif(marks>=70 ):
    print(f'{common_string} B')

elif(marks>=50 ):
    print(f'{common_string} C')
elif(marks>=30):
    print(f'{common_string} D')
else:
    print(f'{common_string} E')
'''


# ========= day-6  18/08/2025 ===========
# loops

# numbers=[1,2,3,4,5]
# for i in numbers:
#     # increment=i
#     # increment+=10
#     # print(f'increment by {i} = {increment}')
#     print(f'increment by 10 on {i} = {i+10}')

# sum=0
# for i in numbers:
#     sum+=i
# print(sum)   


# find the maximum element in the list 
'''numbers=[-5,-1,-10]
max_num=numbers[0]
min_num = numbers[0]
for i in numbers:
        if(i>max_num):
            max_num=i
        if i < min_num:
            min_num = i

        


print(f"maximum element in {numbers} ={max_num} and minimum element ={min_num}")
'''


# # find all even number  and odd number in a list

# number=[1,2,3,4,5,6,7,8]

# even=[]
# odd=[]
# for num in number:
#     if(num%2==0):
#         even.append(num)
#     else:
#         odd.append(num)   

# print(even,end="\n")
# print(odd,end="\n")
# # length of character in a string

# name ="arun kumar sharma"
# count =0
# for i in name:
#     if(i != ' '):
#         count+=1

# print(f"length of {name} = {count}")

#  ============= 19/08/2025 ====================

# merge two sorted list and then sorted the new list

# a=[1,2,3,4,5,6,7,8,10,12,14]
# b=[9,11,13,15]
# c=[]

# for num in a:
#     isDuplicate=False
#     for num2 in b:
#         if(num==num2):
#             isDuplicate=True
#             continue
#         elif (num<num2):
#             c.append(num)
#         else:
#             c.append(num2)    
    
# print(c)


# data={'name':'anmol','class':12,'Roll_number':20}
# for key in data:
#     print(f"key = {key} value ={data[key]}")



# range functions

# for i in range(1,10,2): # 2-1 ko chhodega -->first is inclusive,second is exclusive, and third one is  step size
#     print(i) #0 ... 9  0,2,4,6,8

# for i in range(10,0,2):
#     print (i)

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)    

# number1=int(input("enter first number: "))
# number2=int(input("enter second number: "))

# even=[]
# for i in range(number1,number2+1):
#     if(i%2==0):
#         even.append(i)


# print(even)


#  =========== 20/08/2025
# number =int(input("Enter the number to get it's sum from 1: "))

# sum=0
# i=1
# while(i<=number):
#     sum+=i
#     i+=1

# print(sum)    


# while(True): #true/1
#     name =input("Enter your name: ")
#     if(name==''):# when no input/directly user press the enter
#         print('program has been ended!')
#         break
#     else:
#         print(f'you entered {name}')



# 16 1--->1000

# for i in range(1,1001):
#     if(i==16):
#         print(f"{i} founded...")
#         break;    

# i=1
# while(i<=1000):
#     if(i==16):
#         print(f'yes {i} is founded')
#         break
#     i+=1;     
# print("this will run")

   
# i=0  #0
# while(i<=10): #0 1 2 3 4 5 6 7 8 9 10
#     if(i==5): #0==5 f,1==5 f , ... 5==f t
#         i+=1
#         continue
#     print(i)    
#     i+=1 
  
# i=5
# def increment():
#     i==5
#     if(i==5):
#         break
#     print(i)            
# increment()
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)    


#! Print only even numbers between 1 and 20 using continue to skip odd numbers.
'''
        i=1
        while(i<21):
            if(i%2 != 0):
                i+=1
                continue
            print(i)    
            i+=1 
'''
#! Create a program that prints characters of the string "python", but stop printing if the character is 'h'.
'''
        name='python'
        i=0
        while(True):
            if(name[i]=='h'):
                break
            print(name[i])        
            i+=1    
'''

#! Find the first number divisible by both 3 and 7 in the range 1–100. (Use break).


# *   ============== 21/08/2025 ===========


# get input from user and check it is prime or not
''' 
    number=int(input("enter number to get while it is prime or not: "))

    # example number=10
    if(number<=1):  #10<=1 false
        print(f"Enter valid number to check,  {number} is not valid")



    # 36= 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 --- 36

    else:
        i=2
        isPrime=True
        while(i*i<=number): #4<=10 or 2<=underroot 10, i.e 2<=3.162
            if(number%i == 0):
                isPrime=False
                break   #outside the loop
            i+=1

        if(isPrime): #false ,not executed
            print(f"{number} is prime!") 
        else: # executed
            print(f" {number} is not prime!")    
'''

# 50 se neeche sabhi prime chhapo

'''
    prime=[]

    number=50
    i=2

    # i =2 3 4 5 6  .... 50
    while(i<=number):
        j=2
        isPrime=True
        while(j<i): #j one by one increment hoga
            if(i%j==0):
                isPrime=False
                break #nested loop ends
            j+=1     
            
        if(isPrime):
            prime.append(i)

        i+=1   

    print(prime)    
'''


#* ========================== 22/08/2025 ============

# def sum(a,b):
'''
    def sum(*args):
        a,b=args
        return a+b

    print(sum(10,20))
'''


# maximum element in list 

'''
    def maxElement(*args):
        return max(args)

    print(maxElement(10,40,5,2,30,3))
'''
    
# pass dictionary as an argument and acces it

'''

    def userInfo(**args): #**
        for key,value in args.items():
        print (f"{key} = {value}")

    userInfo(name="anmol",age=50,salary="2.4 cr")
'''


# 6 as 36 with return

# def squareNumber(number):
#     return number**2

# print(squareNumber(int(input("enter number to get its square value: "))))



#! check whether number is prime or not

'''
    def primeCheck(a):
        if(a<=1):
            return f"{a} is not a prime"
        i=2
        isPrime=True
        while(i*i<=a):
            if(a%i==0):
                isPrime=False
                break   
            i+=1
    
        if(isPrime):
            return f"{a} is prime"
        else:
            return f"{a} is not prime" 

        

    print(primeCheck(int(input("Enter number to check while it is prime or not! "))))
'''


#! lambda function
'''
    A lambda function in Python is just a small anonymous function.
    Anonymous means it doesn’t need a name like def myFunc(): ....
    It’s usually used when you need a function for a short time. 
    lambda arguments: expression
'''

# square = lambda x:x**2
# print(square(5))

# add =lambda x,y:x+y
# print(add(10,20))

# add =lambda x,y=20:x+y
# print(add(10))


#* ======== 25/08/2025 =========== 



# def Even(numbers):

#     return list(filter(lambda x:x%2==0,numbers))      
    
# numbers=[2,4,6,7,8,40,50,2,56]

# # print(Even(numbers))


# def  add_20_to_each(numbers):
#     return list(map(lambda x:x+20,numbers))

# print(add20Each(numbers))


#! data =[("Vishal", 123), ("Arun", 133),("Chetan", 150)]
#! sorted_data = sorted(data,key=lambda x:x[1],reverse=True)
#! print(sorted_data)


''' 
    def Check_Prime(N):
        if(N<=1):
            return False
        else:
            for i in range(2,N):
                if N%i==0:
                    return False
        return True  

    n=int(input("Enter Number to check it is prime or not.: "))  

    print(f"{n} is prime number") if Check_Prime(n) else print(f'{n} is not a prime') 
'''


def check_individual_prime(Number):
    isPrime=True
    i=2
    while i*i<=Number:
        if Number%i==0:
            isPrime=False
            break
        i+=1    
    if isPrime:
        return True
    else:
        return False        

# def check_prime(N):
#     if(N<=1):
#         return f"invalid input {N}"
#     else:
#         new_list=[]
#         for i in range(2,N+1):
#             if check_individual_prime(i):
#                 new_list.append(i)
#         return new_list

      
# print(check_prime(int(input("Enter Number: "))))

#* ======================== 26/08/2025 ========================== 

# find nth prime number 
'''
Program to find the nth prime number
Approach: 
- Start from i = 2
- Check if i is prime by testing divisors up to √i
- Count primes until we reach the given position
'''

'''



def primeNumberAt(position):
    count = 0
    i = 2
    
    while True:
        if check_individual_prime(i):
            count += 1
            if count == position:
                return i
        i += 1
user_input = int(input("Enter a number to get the prime number at that position: "))
print(primeNumberAt(user_input))
'''

'''
    def Sum_of_n_Prime_Number(number):
        i=2
        Sum=0
        count=0
        while(True):
            if check_individual_prime(i):
                count+=1
                Sum+=i
                if(count==number):
                    return Sum
            i+=1        

    print(Sum_of_n_Prime_Number(int(input("Enter a number to get the sum of all prime numbers up to that number:"))))
'''

# find Prime Factorization of number n
# def Prime_Factor(number): 
#     prime=[]
#     i=2
#     while i<=number:
#             if number%i==0: 
#                 number=int(number/i)
#                 prime.append(i)
#             else:
#                 i+=1
#     return prime
# number =int(input("Enter Number to get it's Prime Factor: "))
# print(Prime_Factor(number))



#! 84/2 42/2 21/3 7/7  question--> 2 2 3 7
#! unique 2 3 7
# find Prime Factorization of number n

# def unique_prime_factors(number):
#     i=2
#     prime=[]
#     while i<=number:
#         if number%i==0:
#             number= int(number/i)
#             prime.append(i)
#         i+=1  
#     return prime    

# print(unique_prime_factors(int(input("enter no. to get unique prime factors: "))))




#! highest prime factor e.g=7 
# def highest_prime_factor(number):
#     i=2
#     highest=1
#     while i<=number:
#         if number%i==0:
#             number= int(number/i)
#             if(i>highest):
#                 highest=i
#         i+=1  
#     return highest    

# print(highest_prime_factor(int(input("enter no. to get Highest prime factors: ")))) 


#* ===================28/08/2025==========================

# str1="apple"
# str2="banana"

# print(str1>str2) #'a'=97>'b'=98  97>98,false
# print(str1<str2) #'a'=97>'b'=98  97<98,true
# print(str1==str2) #false

# str1="apple"
# str2="Apple"

# print(str1>str2) #'A'=65>'a'=97  97>65,true
# print(str1<str2) #'a'=97>'A'=65  97<65,false
# print(str1==str2) #97==65,false

# str1="cat"
# str2="caterpiller"

# jaise hi ek string khatm ho jaegi use chhota consider krdiya jaaega
# print(str1>str2) #false
# print(str1<str2) #true
# print(str1==str2) #false


#! unicode 
# print(ord('A'))#65
# print(ord('a'))#97
# print(ord(' '))#32
# print(ord('0'))#48


# str="Anmol"

# count =0
# for i in str:
#     count+=1

# print(count)    

#!create a classs bankaccount  and create constructor to initialize the account holder name and initialize the account balance

#? create 3 function name credit,withdraw and check balance to perform these operation 

# class bankaccount:
#     def __init__(self,name,account_balance):
#         self.name=name
#         self.account_balance=account_balance
#     def credit(self,amount):
#         self.account_balance+=amount
#     def withdraw(self,amount):
#         if amount>self.account_balance:
#             return 'insufficient fund'
#         else:
#             self.account_balance-=amount
#             return f"Withdrawal successful"

#     def check_balance(self):
#         return self.account_balance

# customer1=bankaccount("anmol",1000)
# credit=customer1.credit(200)
# credit=customer1.credit(1000)

# print(customer1.withdraw(2000))#Withdrawal successful
# print(customer1.withdraw(1000))#insufficient fund
# print(customer1.check_balance())

#* ==================== 29/08/2025================== 

# name="AnMoL"

# capital to lower

# for i in name:
#     if(i>='A'and i<='Z'):
#         i=chr(ord(i)+32)
#         new_name+=i
#     else:
#         i=chr(ord(i)-32)
#         new_name+=i   
        
# print(new_name)


# string="python is a fun" # fun is a python
# print(string.split()) # ['python', 'is', 'a', 'fun']

# data=['python', 'is', 'a', 'fun']
# print(" ".join(data))




# string="python is a fun"
# print(string.find("is")) #7
# print(string.startswith("py")) #true

#! reverse  string

# string="Aman"

# print(string[::-1])

# print("".join(reversed(string)))

#? reverse string
# length=len(string)
# i=0
# chars = list(string)
# print(chars) # ['A', 'm', 'a', 'n']
# while(i<length):
#     temp=chars[i]
#     chars[i]=chars[length-1]
#     chars[length-1]=temp
#     length-=1
#     i+=1
# string="".join(chars)   
# print(string)    

# ? pyhton is fun ==>fun is python

# string="python is fun language"
# string_list=[]
# currword=""
# for i in string:

#     if i != " ":
#         currword+=i
#     else:
#         string_list.append(currword)
#         currword="" #reset
# if currword:
#     string_list.append(currword)


# i=0
# length=len(string_list)
# while(i<length):
#     temp=string_list[i]
#     string_list[i]=string_list[length-1]
#     string_list[length-1]=temp
   
#     i+=1
# print(" ".join(string_list))    


#! 
# words=["python","is","fun"]

# i=0
# length=len(words)
# while i<length:
#     words[i],words[length-1]=words[length-1],words[i]
#     length-=1
#     i+=1
# print(" ".join(words).strip())    


#!homework  python is fun ==> nohtyp si nuf

#! 1
# string ="python is fun"
# string_list=string.split()

# for i in range(0,len(string_list)):
#     string_list[i]=string_list[i][::-1]
   
    
    
# print(" ".join(string_list))
#* ================================= 01/09/2025============================
#!2 
# string ="python is fun"
# string_list=string.split()
# new_list=[]
# for i in string_list:
#     reverse=""
#     for j in i:
#         reverse=j+reverse
    
#     new_list.append(reverse)
  
# print(" ".join(new_list))

#! check whether the string is palidrome or not

# def Reverse(word):
#     reverse=""
#     for i in word:
#         reverse=i+reverse
#     return reverse

# def palidrome(input):
#     reverse=Reverse(input)
#     if(input==reverse):
#         return True
#     else:
#         return False    

# while(True):
#     user_input=input("Enter the word to check: ")
#     if user_input:
#         print(palidrome(user_input))
#     else:
#         break



#! count vowel in a string
# def countVowel(word):
#     # vowel="aeiouAEIOU"
#     count=0
#     for i in word:
#         # for j in vowel:
#         for j in "aeiouAEIOU":
#             if j==i:
#                 count+=1
#                 break
#     return count  


# string ="anmol panday"
# print(countVowel(string))
    

#! ===========list ================
list_1=[1,2,3]
# list_2=[1,2,3]

#?concatenate
# print(list_1+list_2) 

#? repeat same thing 
# print(list_1*3)  #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#? membership
# for i in list_1:
#     print(i)

#? reverse
# print(list_1[::-1]) 

#? sort
# print(sorted(list_1)) 

#? find the secod highest in a list 
# new_list={40,1,2,20} #output should be 20
# sorted_list=sorted(new_list)
# length=len(sorted_list)
# user_input=int(input("which highest you want: "))
# highest=sorted_list[length-user_input]
# print(f"{user_input} highest: {highest}")

#? insert  remove pop
new_list=[40,1,2,20] 
#! new_list.insert(0,10)
# print(new_list)
#! new_list.remove(10)
# print(new_list)

# new_list.pop()
# print(new_list) #remove last if not index provide in argument

#? count ,reverse ,clear
# print(new_list.count(1))#return how many time element appear
# new_list.reverse()
# print(new_list)
# new_list.clear()
# print(new_list) #empty list 

#*** tuple is homework 


#>>===========hw===================<<

string =".isalphac1" # .1cahplasi
# string ="a.byc3" # 3.cyba
string_list=list(string)
# for i in range(length):
i=0
length=len(string_list)
while(i<length):
    if string_list[i]!='.':
        string_list[i],string_list[length-1]=string_list[length-1],string_list[i]
        length-=1
        i+=1
    else:
        i+=1  
expected_string="".join(string_list)          
print(expected_string)    
