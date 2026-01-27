# 6. Write a lambda function which accepts one number and returns True if number is odd
#    otherwise False.

Even = lambda No : (No % 2 == 1)
    
def main():
    
    print("Enter  Number :")
    No = int(input())
    
    ret = Even(No)
    if ret == True:
        print(f"{No} is Odd as it returns : {ret}")
    else:
        print(f"{No} is Even as it returns : {ret}")
            
if __name__=="__main__":
    main()