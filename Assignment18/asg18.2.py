# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56 

def MaxList(list):
    
    Max = list[0]
    
    for i in range(len(list)):
        if list[i] > Max:
            Max = list[i]
        
    return Max


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
    
    ret = MaxList(list)
    
    print("Max elements of list is : ",ret)
    
if __name__ == "__main__":
    main()