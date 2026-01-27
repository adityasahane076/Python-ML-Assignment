# 6.Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero 

def ChkNum(No):
    if No > 0:
        print("Positive")
    elif No < 0:
        print("Negative")
    elif No == 0:
        print("Zero")
    else:
        print("Invalid input")
def main():
    
    print("Enter  Number :")
    No = int(input())
    
    ChkNum(No)
    
if __name__=="__main__":
    main()