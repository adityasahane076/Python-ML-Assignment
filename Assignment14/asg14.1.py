# 1. Write a lambda function which accepts one number and returns square of that number.

Square = lambda No : No * No
    
def main():
    
    print("Enter  Number :")
    No = int(input())
    
    ret = Square(No)
    print(f"Square of {No} is {ret}")
            
if __name__=="__main__":
    main()