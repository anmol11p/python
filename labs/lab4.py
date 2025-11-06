
#!Q1 write a python program to count all letters,digits and symbols from the given string 
# input = "P@#yn26at^&i5ve"

# def count_letters_digits_symbols(string):
#     letter_count=0
#     symbol_count=0
#     digit_count=0
#     for elem in string:
#         if 65<=ord(elem)<=90 or 97<=ord(elem)<=122:
#             letter_count+=1
#         elif 48<=ord(elem)<=57:
#             digit_count+=1
#         else:
#             symbol_count+=1
#     return letter_count,digit_count,symbol_count            


# letter_count,digit_count,symbol_count= count_letters_digits_symbols("P@#yn26at^&i5ve")
# print (f"letters: {letter_count} ,digits: {digit_count} , symbols: {symbol_count}")


#!Q2 write a python program to remove duplicate characters of a given string:

# def remove_duplicate_words(sentence):
#     uniqueWordSentence=[]
#     # convert string into list 
#     sentence_list=sentence.split()
#     for elem  in sentence_list:
#         if elem not in uniqueWordSentence:
#             uniqueWordSentence.append(elem)
#     # conver list to string again            
#     return " ".join(uniqueWordSentence)                 

# Input="String and String function"

# print(remove_duplicate_words(Input))


#! Q3 write a program to count uppercase,lowercase,special character and numeric values in a string



# def analyze_string(string):
#     analyze_dict={"upperCase":0,"lowerCase":0,"special_character":0,"number":0}
#     for elem in string:
#          if 97<=ord(elem)<=122:
#               analyze_dict["lowerCase"]+=1
#          elif 65<=ord(elem)<=90:
#               analyze_dict["upperCase"]+=1
#          elif 48 <=ord(elem)<=57:
#               analyze_dict["number"]+=1
#          else:
#               analyze_dict["special_character"]+=1
#     return analyze_dict;                        
              
              
# print(analyze_string("Hell0 W0rld ! 123 * # welcome to pYtHoN"))    


#! Q4 write a python prgm to  count vowels in a string

# def count_vowels(string):
#         count=0
#         for elem in string:
#                 if elem in "aeiouAEIOU":
#                         count+=1
#         return count

# print(count_vowels("Welcome to Python Assignment"))