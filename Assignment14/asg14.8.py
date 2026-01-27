# 8. Write a lambda function which accepts two numbers and returns addition.

Add = lambda No1,No2 : No1 + No2
    
def main():
    
    print("Enter  Number 1:")
    Value1 = int(input())
    
    print("Enter  Number  2:")
    Value2 = int(input())
    
    ret = Add(Value1,Value2)
    
    print(f"Addition of the numbers is {ret}")
            
if __name__=="__main__":
    main()