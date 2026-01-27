# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of
# all elements.

from functools import reduce

def main():
    
    Data = [2,3,14,5,6,7,8,9]
    
    Add = reduce(lambda No1, No2 :No1 + No2,Data)
    
    print("The Addition of list is : ",Add)
    
if __name__ == "__main__":
    main()