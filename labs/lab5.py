
#!Q1 WRITE A PYTHON PROGRAM TO SUM ALL THE ITEMS IN A LIST 

# def sum_of_all_elem(List):
#     SUM=0
#     for elem in List:
#         SUM+=elem
#     return SUM
# new_list=[1,2,3,4,5,6,7]
# print(sum_of_all_elem(new_list))


# ! Q2   WRITE A PYTHON PROGRAM TO GET THE LARGEST AND SMALLEST NUMBER FROM A LIST WITHOUT  BUILTIN FUNCTIONS

# def get_largest_and_smallest(given_list):
#     smallest=given_list[0]
#     largest=given_list[0]
#     for elem in given_list:
#         if elem<smallest:
#             smallest=elem
#         if elem>largest:
#             largest=elem
#     return f"smallest number= {smallest}\nlargest number= {largest}"                


# print(get_largest_and_smallest([4,5,80,1,0,5,-1,4]))  

#! Q3 WRITE A PYTHON PROGRAM TO FIND DUPLICATE VALUES FROM A LIST AND DISPLAY THOSE.

# def find_duplicate_values(given_list):
#     seen=set()
#     duplicate=[]
#     for elem in given_list:
#         if elem in seen and elem not in duplicate:
#             duplicate.append(elem)
#         else:
#             seen.add(elem)    
#     return duplicate

# print(find_duplicate_values(["anmol","panday","anmol"]))

#! Q4 WRITE A PYTHON PROGRAM TO SPLIT A GIVEN LIST INTO TWO PARTS WHERE THE LENGTH OF THE FIRST PART OF THE LIST IS GIVEN


# def split_list(givenlist,firstpartlength):
#     i=0
#     firstpart=[]
#     secondpart=[]
#     while i<firstpartlength:
#         firstpart.append(givenlist[i])
#         i+=1
#     j=firstpartlength
#     while j<len(givenlist):
#         secondpart.append(givenlist[j])  
#         j+=1  
#     return firstpart,secondpart 

# print(split_list([1, 2, 3, 4, 5, 6, 7],3))    

#! Q5 WRITE A PYTHON PROGRAM TO TRAVERSE A GIVEN LIST IN REVERSE ORDER, AND PRINT  THE ELEMENTS  WITH THE ORIGINAL INDEX

def reverse(given_list):
    result=[]
    i=len(given_list)-1
    while i>=0:
        result.append(f"Index:{i} Element:{given_list[i]}")
        i-=1
    return result


print(reverse(['red','green','white','black']))