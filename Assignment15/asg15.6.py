# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum
# element.

from functools import reduce

def main():
    
    Data = [2,3,14,5,6,1,8,9]
    
    Min = reduce(lambda No1, No2 :No1 if No1 < No2 else No2,Data)
    
    print("The Minimum of list is : ",Min)
    
if __name__ == "__main__":
    main()