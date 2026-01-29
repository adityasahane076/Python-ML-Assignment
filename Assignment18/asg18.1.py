# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130 

def AdditionList(list):
    
    Sum = 0
    
    for i in range(len(list)):
        Sum = Sum + list[i]
        
    return Sum


def main():
    
    list = []
    NoElements = 0
    
    print("Enter Number of Elements : ")
    NoElements = int(input())
    
    print("Enter Elements : ")
    
    for i in range(NoElements):
        Value = int(input())
        list.append(Value)
    
    print(list)
    
    ret = AdditionList(list)
    
    print("Sum of elements of list is : ",ret)
    
if __name__ == "__main__":
    main()