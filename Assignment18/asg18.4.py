# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def MinList(list,No):
    
    Freq = 0
    
    for i in range(len(list)):
        if list[i] == No:
            Freq = Freq + 1
        
    return Freq


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
    
    print("Enter the Element to search : ")
    Element = int(input())
    
    ret = MinList(list,Element)
    
    print(f"Frequency of {Element} in list is : ",ret)
    
if __name__ == "__main__":
    main()