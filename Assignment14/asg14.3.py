# 3. Write a lambda function which accepts two numbers and returns maximum number.

Max = lambda No1,No2 : (No1 > No2 ) 
    
def main():
    
    print("Enter  Number :")
    Value1 = int(input())
    
    print("Enter  Number :")
    Value2 = int(input())
    
    ret = Max(Value1,Value2)
    if ret == True:
        print(f" {Value1} is Maximum")
    else:
        print(f"{Value2} is Maximum")
            
if __name__=="__main__":
    main()