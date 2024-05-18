# Find Maximum of two numbers in Python
# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1
# a=2
# b=4
# c=max(a,b)
# print(c)

# # second method
# if(a>b):
#     print(a)
# else:
#     print(b)

# third method using function
# def max_custom(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>c ):
#         return b
#     else:
#         return c
    
# print(max_custom(12,5,18))

# fourth method
def max_custom(*args):
    maximum_value=args[0]
    for i in range(1,len(args)):
        if(args[i]>maximum_value):
            maximum_value=args[i]
    return maximum_value

            
    

            
    
    
print(max_custom(12,5,18,78,96,87))
