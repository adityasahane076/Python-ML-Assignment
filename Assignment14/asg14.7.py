# 7. Write a lambda function which accepts one number and returns True if divisible by 5.


Even = lambda No : (No % 2 == 1)
    
def main():
    
    print("Enter  Number :")
    No = int(input())
    
    ret = Even(No)
    if ret == True:
        print(f"{No} is Divisible by 5 as it returns : {ret}")
    else:
        print(f"{No} is not Divisible by 5 as it returns : {ret}")
            
if __name__=="__main__":
    main()