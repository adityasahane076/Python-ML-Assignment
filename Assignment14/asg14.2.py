# 2. Write a lambda function which accepts one number and returns Cube of that number.

Cube = lambda No : No **3
    
def main():
    
    print("Enter  Number :")
    No = int(input())
    
    ret = Cube(No)
    print(f"Cube of {No} is {ret}")
            
if __name__=="__main__":
    main()