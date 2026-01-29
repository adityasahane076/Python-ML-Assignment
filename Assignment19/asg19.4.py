# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204  

from functools import reduce

def main():
    
    Data = []
    
    print("Enter Number of Elements : ")
    length = int(input())
    
    print("Enter Elements :")
    for i in range(length):
        element = int(input())
        Data.append(element)
    
    FData = list(filter(lambda No : (No % 2 == 0),Data))
    
    
    MData = list(map(lambda No: No ** 2 , FData))
    
    RData = reduce(lambda No1,No2:No1+No2, MData)
    
    print("Actual Data : ",Data)
    print("The Filtered list  is : ",FData)
    
    print("List after map is : ",MData)
    
    print("After Reduce : ",RData)
    
if __name__ == "__main__":
    main()