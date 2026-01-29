# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5 

def MinList(list):
    
    Min = list[0]
    
    for i in range(len(list)):
        if list[i] < Min:
            Min = list[i]
        
    return Min


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
    
    
    ret = MinList(list)
    
    print("Min elements of list is : ",ret)
    
if __name__ == "__main__":
    main()