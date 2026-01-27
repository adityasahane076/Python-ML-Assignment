#2. Write a program which contains one function named as ChkNum() which accept one
# parameter as number. If number is even then it should display “Even number” otherwise
# display “Odd number” on console.
# Input : 11 Output : Odd Number
# Input : 8 Output : Even Number

def ChkNum(No):
    if No % 2 == 0:
        return True
    else:
        return False
def main():
    
    print("Enter  Number :")
    No = int(input())
    
    ret = ChkNum(No)
    
    if ret == True:
        print(f"{No} is a Even number")
    else:
        print(f"{No} is Odd number ")
            
if __name__=="__main__":
    main()