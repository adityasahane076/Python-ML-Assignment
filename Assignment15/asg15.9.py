# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all
# elements.

from functools import reduce

def main():
    
    Data = [2,3,14,5,6,7,8,9]
    
    Product = reduce(lambda No1, No2 :No1 * No2,Data)
    
    print("The Product of the list is : ",Product)
    
if __name__ == "__main__":
    main()