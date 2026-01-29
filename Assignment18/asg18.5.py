#5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5) 

from MarvellousNum import ChkPrime

def ListPrime(list):
    
    Sum = 0
    
    for i in range(len(list)):
        bflag = ChkPrime(list[i])
        
        if bflag == True:
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

    
    ret = ListPrime(list)
    
    print("Sum of Prime elements in list is : ",ret)
    
if __name__ == "__main__":
    main()