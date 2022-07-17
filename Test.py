#A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning true if the integer is pandigital, and false otherwise.
#Sample input : 1234567890
#Output : True
 
Sample input : 1123456890
Output : False
 
def	is_pandigital_num(num):
    numList=[0,1,2,3,4,5,6,7,8,9]
    
    for i in numList:
        if i in str(num):
            continue
        else:
            return False

    return True

