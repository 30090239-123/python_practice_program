# Python program to interchange first and last elements in a list
"""Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]"""

list1=[1, 2, 3]
n=len(list1)
temp=list1[0]
list1[0]=list1[n-1]
list1[n-1]=temp
print(list1)
