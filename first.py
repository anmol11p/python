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


# class college():
#     collegename="Jb knowledge park"
#     def __init__(self,name,age):
#         self.name=name  #instance variable
#         self.age=age    #instance variable  

# student1=college("anmol",23)
# student2=college("anubhav",21)

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

# string =".isalphac1" # .1cahplasi
# # string ="a.byc3" # 3.cyba
# string_list=list(string)
# # for i in range(length):
# i=0
# length=len(string_list)
# while(i<length):
#     if string_list[i]!='.':
#         string_list[i],string_list[length-1]=string_list[length-1],string_list[i]
#         length-=1
#         i+=1
#     else:
#         i+=1  
# expected_string="".join(string_list)          
# print(expected_string)    



#*==================== 2/09/2025========================

#!Dictionary

# key-->unique
# value-->can repeat
# define {} or dict()

#? name roll_number

# dictionary={"name":"Anmol","roll_number":23}

# for key in dictionary:
#     print(f"{key}: {dictionary[key]}")

#! set

SET={1,2,3}
# SET2={3,4,5}
# # print(SET | SET2) #union
# # print(SET & SET2) #intersection
# print (SET-SET2) #difference-> 1,2
# # print(SET ^ SET2) #intersection ko hatake sara dedega


# #?issubset disjoint 
# A = {1, 2}
# B = {1, 2, 3}


#!pattern
# n=int(input("enter number: "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")   
#     print()  

#? triangle 
# n=int(input("enter number: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()    


#*==============  3/09/2025============================

#! OOPS

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


# student1=Student("anmol",23) #constructor called
# print(student1.age)
# print(student1.name)



#? question

# def get_length_marks(marks):
#     total=0
#     length=0
#     for mark in marks:
#         total+=mark
#         length+=1
#     return total,length    

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def average(self):
#         total,length=get_length_marks(self.marks)
#         average=total/length
#         return average
# s1=Student("anmol",[20,30,40])
# print(s1.average())

# !encapsulation
# class userAuthentication:
#     def __init__(self,username,password):
#         self.username=username
#         self.__password=password #private,access modifier
#     def set_password(self,password):
#         self.__password=password    
#     def get_user(self):
#         return f"user= {self.username} password= {self.__password}"

# user1=userAuthentication("anmol",123456789)
# # password change
# user1.set_password("Anmol0031@")
# print(user1.get_user())

#!Inheritance 

#? single inheritance 
# class Animal:
#     def speak(self):
#         return 'animal can speak'
#     def tail(self):
#         return 'animal has tail'

# class dog(Animal):
#     def bark(self):
#         return 'dog is barking'

# d1=dog()
# # print(d1.bark())#own method        
# print(d1.speak())#parent method        

#? multilevel inheritance 
# class Animal:
#     def speak(self):
#         return 'animal can speak'
#     def tail(self):
#         return 'animal has tail'

# class cow(Animal):
#     def tail(self):
#         return 'cow has tail'

# class jersey(cow):
#     def breed(self):
#         return 'jersey is a breed of cow'

# j1=jersey()
# print(j1.breed())#own method        
# print(j1.tail())#cow        
# print(j1.speak())#animal

#? Multiple inheritance
# * child have multiple parent*

# class Mother:
#     def skills(self):
#         print('mother: cooking')
# class Father:
#     def skills(self):
#         print('father: gardening')
# class Child:
#     def skills(self):
#         print('child: Coding')
# c = Child()
# c.skills()    #overrides the parent     

#? Hierarchical inheritance
#* Same parent to all the subclasses ,such that all are sibling *#

# * ==================== 4/09/2025========================================

#! polymorphism
# method overriding

# class Vehicle:
#     def run(self):
#         print("vehicle run")
# class Car(Vehicle):
#     def run(self):
#         print("car run")
# class Bike(Vehicle):
#     def run(self):
#         print("bike run")

# def make_run(vehicle):
#     vehicle.run()
# B1=Bike()
# C1=Car()
# make_run(B1)
# make_run(C1)


#? operator overloading 

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         # Overloads the + operator for Point objects
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         # Defines the string representation
#         return f"Point({self.x}, {self.y})"

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2  # Uses the overloaded __add__ method
# print(p3)      # Uses the overloaded __str__ method


# * =============== 8/09/2025 ==========================

# #? Abstraction

# from abc import ABC, abstractmethod
# class abstractParent(ABC):
#     @abstractmethod
#     def show(self): #jitne bhhi abstract methiod honge unhe body provide karani padegi
#         pass

# class abstractChild(abstractParent):
#     def show(self):
#         print ("show")

# child=abstractChild()
# child.show()
# parent=abstractParent() #* Can't instantiate abstract class abstractParent without an implementation for abstract method 'show'


#! 2 question
    #? Write a program that prevents direct object creation of an abstract class Appliance
    #? Create subclasses WashingMachine and Refrigerator that implement methods like turn_on() and turn_off().
''' 
from abc import ABC,abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Refrigerator(Appliance):
    def turn_on(self):
        print("refrigerator turn on")        
    def turn_off(self):
        print("refrigerator turn off")        
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine turn on")        
    def turn_off(self):
        print("Washing Machine turn off")    
'''    

# wm=WashingMachine()
# wm.turn_on()
# wm.turn_off()
#* ================== 9/09/2025 ============================ 

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# try:
#     output=a/b
# except Exception as e:
#     print(f" you can't divide {a} by 0")

#! handling multiple exception 

# try:
#     output=10/0
# except Exception as e:
#     print(f" you can't divide  by 0")

# else:
#     print("else")
# finally:
#     print("finally!")

#* ============ 10/09/2025=========== 
# for i in range(3):
#     for j in range(3):
#         print(f"i {i} j{j}")


#? right triangle 
# n=4
# for i in range(n+1):
#     for j in range(i):
#         print("*",end=' ')
#     print()    

#? inverse right triangle
# ****
# ***
# **
# *

# n=4
# i=n
# while i>0:
#     for j in range(i):
#         print("*",end="")
#     print()    
#     i-=1    

#?
# 1
# 12
# 121
# 1212
# for i in range(1,5):
#     for j in range(i):
#         if j%2==0:
#             print(1,end="")
#         else:
#             print(2,end="")      
#     print()        

# ? 
# 1
# 23
# 456
# 78910

# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ") 
#         num+=1   
#     print()  

#! 
# 1
# 21
# 121

#! space
#    *
#   **
#  ***     
    
#! when will  finally not execute>>>>>>
    #? infinite loop
    #? os.exit(0)
    #? exception ko galat leliya toh 


#* ======================12/09/2025==================
#raise
# In Python, raise is used to manually trigger an exception (error).
# class UnderAgeError(Exception):
#     pass
# age=-5
# try:
#     if age<18:
#         raise UnderAgeError("You can't vote")
#     elif age<0:
#         raise UnderAgeError("age can't be negative")
# except UnderAgeError as value:
#     print(value)


#! 7 division Error

# class SevendivisionError(Exception):
#     pass

# try:
#     number=8
#     if number %7 != 0:
#         raise SevendivisionError("7 d e")
#     else:
#         print('perfect')    
# except SevendivisionError as e:
#     print(e)        

#! invalid integer input error 

# try:
#     userInput=int(input("enter number: ")) 
#     print('you enter',userInput)
# except ValueError as val:
#     print(val)    


#* ==================== 16/09/2025========================
# crud in file 

# file = open('demo.txt', 'w')
# file.write("i am anmol panday")
# file.close()


# with open('demo.txt', 'r') as file:
#     print(file.read())


# for automatically close the file
#? with open('C:/Users/Administrator/Downloads/google oath.txt', 'r') as file:
    #? one by one 
    # print(file.readline())

    #? complete 
    # content=file.read()
    # for line in content:
    #     print(line)


#? for append (last data not changed)
# with open('demo.txt','a') as file:
#     file.write("hii")
     


#? problem
with open("practice.txt",'w') as file:
    file.write('hello Everyone we are learning File/io using java i like programming in java ')
#** replace all occurence of java witth python

# with open("practice.txt", 'r') as file:
#     content = file.read()

# content = content.replace("java", "python")  
# with open('practice.txt', 'w') as file2:
#     file2.write(content)


#* search if programming is present here or not

# with open('practice.txt','r') as file:
#     content =file.read()
#     if not content.find('programming')== -1:
#         print('present')
#     else:
#         print("absent")    


#* ==================== 17/09/2025==============================

# square=[]
# for num in range(1,11):
#     square.append(num**2)

# print(square)


#? by list comprehension
# new_square=[num**2 for num in range(1,11)]
# print(new_square)

#* list of even number in list 

# list_even=[num for num in range(1,11) if num%2==0]
# print(list_even)


#?ternary operator

#! Even or Odd

# results=["even" if num%2==0 else "odd" for num in range(1,11)]
# print(results)

#! Replace negative numbers with 0
# nums = [-3, -1, 0, 2, 5]
# results=[0 if num<0 else num for num in nums]
# print(results)


# * ================================= 18/09/2025==========================
# 1-8 table by list comprehension

# table=[]
# for num in range(1,9):
#     subTable=[]
#     for num2 in range(1,11):
#         subTable.append(num2*num)
#     table.append(subTable)    
# print(table)


# table=[[num*i for i in range(1,11) ] for num in range(1,9)]
# print(table)



# arr=[[1,2,3],
#      [4,5,6],
#      [7,8,9],
#      [10,11,12]
#      ]

# new_arr=[]
# for sublist in arr:
#     for elem in sublist:
#         new_arr.append(elem)
# print(new_arr)        



# print("======================using list comprehension=================================")

# arr=[[1,2,3],
#      [4,5,6],
#      [7,8,9],
#      [10,11,12]
#      ]

# emp_arr=[elem for sublist in arr for elem in sublist]
# # emp_arr=[elem**2 for sublist in arr for elem in sublist]
# print(emp_arr)



#* Dictionary comprehension


#!first unique/non repeating 
# string="swiss"

# for char in range(len(string)):
#     unique=""
#     isUnique=True
#     for j in range(len(string)):
#         if(char != j and string[j] == string[char] ):
#             isUnique=False
#             break
#     if isUnique:
#         print(string[char])
#         break


# *=================================19/09/2025=====================================

#!by dictionary   
# string="swiss"
# freq={}

# for s in string:
#     freq[s]=freq.get(s,0)+1

# print(freq)    



#?
# l1=[1,3,5,6]
# l2=[2,4,7,8]
# print(sorted(l1+l2))

import sys
def list_one_to_1000():
    return [i for i in range(1001)]
lst = list_one_to_1000()    
# print(sys.getsizeof(lst)) #8856
# print(len(lst))           #1001


# generator
'''
    def list_one_to_1000():
        i=1
        while i<1001:
            yield i
            i+=1


    gen = list_one_to_1000()
    print(sys.getsizeof(gen)) #184
'''
#! yield is like a pause-and-resume button for a function.
#! Instead of returning all results at once, it produces values one by one when you loop through it (or call next() on it).


#* =================== 22/09/2025============================= 
#? fibonacci series

# def fib(n):
#     a=0
#     b=1
#     print(a,end=" ")
#     for i in range(2,n):
#         next_= a+b 
#         print(next_,end=" ")
#         a=b
#         b=next_
# fib(10)


#? with generator 
# def fib(n):
#     a=0
#     b=1
#     i=0
#     while i<n:
#         yield a
#         a,b=b,a+b
#         i+=1

# for num in fib(5):
#     print(num)


#? list comprehension with generator 

#* gen=(i for i in range(11))
#* print(gen)
#* for i in gen:
#*     print(i)

#? tuple comprehension
# tup=tuple(i for i in range(11))
# print(tup)

 
# ? how to check element is iterable or not
from collections.abc import Iterable
nums=[1,2,3]
# print(Iterable)
# print(isinstance(nums,Iterable))

#! internal working of iterator
# nums = iter(nums)  # convert the list into an iterator

# try:
#     while True:
#         print(next(nums))
# except Exception as e:
#     # print(e) #print empty space
#     print("Iteration has ended!") 


#! implement my range own 
# class Myrange():
#     def __init__(self,curr,end):
#         self.curr=curr
#         self.end=end 
#     # def __iter__(self):
#     #     return self
#     def __next__(self):
#         if self.curr>=self.end:
#             raise StopIteration
#         value=self.curr
#         self.curr+=1
#         return value        


# obj=Myrange(1,5)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# for i in Myrange(1, 5):
#     print(i)



#? Decorator-pdna hai and all thing revise
# it allow you to modify the behaviour of function and methods

def greet(fx):
    print("good morning")
    fx()
    print("thanks for using this function")

# def hello():
#     print("helloworld!")
#? hello=greet(hello) #decorator called
# print(hello)
#! also 
#? @greet #decorator called
# def hello():
#     print("helloworld!")


#* ================= 25/09/2025===========================

# def timer(x):
#     def decorator(func):
#         def wrapper():
#             for i in range(x):
#                 func()
#         return wrapper
#     return decorator
# @timer(5)
# def greet():
#     print('hello,i am anmol')   
# greet()                 

        

#! dunder function 
# class Student():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name} {self.age}"
#     def __len__(self):
#         return self.age    
# std=Student("anmol",23)
# print(len(std))        


#* important 
# class Adder():
#     def __init__(self,a,b):
#         self.a=a 
#         self.b=b 
#     def __add__(self,other):
#         return Adder(self.a+other.a,self.b+other.b)
#     def __repr__(self):
#         return f"Adder(a={self.a}, b={self.b})"




# a1=Adder(10,20)
# a2=Adder(20,40)
# a3=a1+a2
# print(a3)


# class Imag:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self,other):
#         return Imag(self.a+other.a,self.b+other.b)
#     def __str__(self):
#         return f"({self.a}i+{self.b})"
# c1 = Imag(5, 3j) 
# c2 = Imag(2, 9j)
# c3 = c1 + c2
# print(c3) 


'''
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
    # def equal(self,other):
    #     return self.name==other.name and self.rollno==other.rollno

    # def __eq__(self,other):
    #     return self.name==other.name and self.rollno==other.rollno

#     def __gt__(self,other):
#         return self.rollno>other.rollno
        
        

# s1=Student("anmol",22)
# s2=Student("anmol",21)
# # print(s1.equal(s2))
# print(s1>s2)
'''


# import math
# print(math.pi)
# print(math.sqrt(16))

# from math import sqrt,pow,pi
# print(pi)
# print(sqrt(16))
# print(pow(2,3))

# from module import greet,add
# print(greet())
# print(add(50,60))



# import os

#? print(os.getcwd()) # C:\Users\Administrator\Anudip_Python
#? print(os.listdir()) # ['.git', '.vscode', 'dehradun company practice.py', 'demo.txt', 'first.py', 'lab.py', 'lab2.py', 'lab3.py', 'module.py', 'practice.py', 'practice.txt', 'python', 'readme.md', '__pycache__']

# os.mkdir("hello") if not "hello" in os.listdir() else print("already existed")


# know about sys module 


# * ==============================30/9/025================================
# class Student:
#     def __init__(self,sub1,sub2,sub3):
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3
#     @property
#     def percentage(self):
#         return (self.sub1+self.sub2+self.sub3)/3


# s1=Student(90,91,95)
# print(s1.percentage)
# s1.sub2=85
# print(s1.percentage)
        


#! print the first 10 natural numbers using for loop

# for i in range(11):
#     print(i) 


#! python program to check if the given string is a palindrome

# def isPalindrome(input):
#     reverse=""
#     for i in input:
#         reverse=i+reverse
#     if reverse==input:
#         return True
#     else:
#         return False
# string="madam"
# print(isPalindrome(string))


#! python program to check if a given number is an Armstrong number 
# def isArmstrong(num):
#     # length of number
#      length=0
#      individual=[]
#      actual_num=num
#      while num!=0:
#          reminder=num%10
#          num=num//10
#          length+=1
#          individual.append(reminder)  

#      total_sum=0
#      for i in individual:
#          total_sum+=i**length
#      if total_sum==actual_num:
#          return True
#      else:
#          return False    

# num=153
# print(isArmstrong(num))


#! python program to get the fibonacci series b/w 0 to 50

# def getfibonacci(number):
#     first=0
#     second=1
#     print(first,second,end=" ")
#     while True:
#         next_num=first+second
#         if next_num>50:
#             break
#         print(next_num,end=" ")    
#         first=second
#         second=next_num
        

        

# number=50
# getfibonacci(number)



#!python prgm to check the validity of password input by users


class passwordException(Exception):
    pass

def isValid(pswrd):
    isSymbol=False
    isUpperCase=False
    isLowerCase=False
    isNumeric=False
    isLengthgt6=True if len(pswrd)>6 else False

    try:
        for i in pswrd:
            #? uppercase 
            if  65<=ord(i)<=90:
                isUpperCase=True

            #? lowercase 
            if 97<=ord(i)<=122:
                isLowerCase=True

            #? numbers 
            if 48<=ord(i)<=57:
                isNumeric=True

            #? symbol 
            if not (65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57):
                isSymbol=True 
        if not isUpperCase:
            raise passwordException("atleast one uppercase")
        if not isLowerCase:
            raise passwordException("atleast contain one lowerdcase")
        if not isNumeric:
            raise passwordException("atleast containe one numberic value")
        if not isSymbol:
            raise passwordException("atleast contain one special character")
        if not isLengthgt6:
            raise passwordException("password length should be greater than 6")
        
        if (isUpperCase and isLowerCase and isNumeric and isSymbol and isLengthgt6):
            return "yes, it is a valid password"
    except passwordException as e:
        print(e)


password=input("Enter password: ")
isValid(password)