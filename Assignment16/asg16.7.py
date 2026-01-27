# 7. Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8 Output : False
# Input : 25 Output : True 

def ChkNum(No):
    if No % 5 == 0:
        return True
    else:
        return False
def main():
    
    print("Enter  Number :")
    No = int(input())
    
    ret = ChkNum(No)
    
    if ret == True:
        print(f"{No} is Divisible by 5 as return : {ret}")
    else:
        print(f"{No} is not Divisible by 5 as return : {ret}")
            
if __name__=="__main__":
    main()