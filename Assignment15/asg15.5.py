# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum
# element.

from functools import reduce

def main():
    
    Data = [2,3,14,5,6,7,8,9]
    
    Max = reduce(lambda No1, No2 :No1 if No1 > No2 else No2,Data)
    
    print("The Maximum of list is : ",Max)
    
if __name__ == "__main__":
    main()