# find minimum number in list
def minimum_number(*args):
    minimum_no=args[0]
    for i in range(1,len(args)):
        if(args[i]<minimum_no):
            minimum_no=args[i]
    return minimum_no
print(minimum_number(2,5,6,9,3,9,-3,0))