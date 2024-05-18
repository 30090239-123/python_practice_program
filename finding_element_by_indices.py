# Given two lists with elements and indices, write a Python program to find elements of list 1 at indices present in list 2. 

# Examples:

# Input : lst1 = [10, 20, 30, 40, 50]
#         lst2 = [0, 2, 4]
# Output : [10, 30, 50]
# Explanation: 
# Output elements at indices 0, 2 and 4 i.e 10, 30 and 50 respectively. 

# Input : lst1 = ['Hello', 'geeks', 'for', 'geeks']
#         lst2 = [1, 2, 3]
# Output : ['geeks', 'for', 'geeks']

lst1 = [10, 20, 30, 40, 50]
lst2 = [0, 2, 4]
# for i in range(len(lst2)):
    
#     index=lst2[i]
#     print(index)
    # lst2[i]=lst1[index]
    
# print(lst2)
""" 

step-1 i=o

     index=0,lst2 at i=0
     so,lst1 at index=0 is 10
     so,updating value 10 at i=0 of lst2 (reutilizing lst2 for response)
     
step-2  i=1
       
       index=2, lst at i=1
       so lst2 at index=2 is 30
       so updating value 30 at i=1 of lst 2
       
step-3 i=2
      
      index=4, lst2 at i=2
      so lst2 at index=4 is 50
      so updating value 50 at i=2 of lst2
      
      
final response is [10,30,50]
    
"""
# Implement second method
# for lst2 in lst1:
#     lst1.append(lst2)
# print(lst2)
response=[]
for item in lst2:
    # print(item)
    response.append(lst1[item])
    
print(response)