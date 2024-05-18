# Input: [2, 3, 5, 6, 7]
# Output: []

# list1=[1,5,7,8,9,16]
# list1.clear()
# print(list1)

# second method
list1=[2,5,6]
for i in range(len(list1)):
    list1.pop()
    print(i)
print(list1)
