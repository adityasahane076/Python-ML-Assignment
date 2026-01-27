# 4. Write a lambda function which accepts two numbers and returns Minimum number.

Min = lambda No1,No2 : (No1 < No2 ) 
    
def main():
    
    print("Enter  Number :")
    Value1 = int(input())
    
    print("Enter  Number :")
    Value2 = int(input())
    
    ret = Min(Value1,Value2)
    
    if ret == True:
        print(f" {Value1} is Minimum")
    else:
        print(f"{Value2} is Minimum")
            
if __name__=="__main__":
    main()