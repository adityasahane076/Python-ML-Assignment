# 10. Write a lambda function which accepts three numbers and returns largest number.

Largest = lambda No1,No2,No3 : No1 if No1 > No2 and No1 > No3 else(No2 if No2 > No3 else No3)
    
def main():
    
    print("Enter  Number 1:")
    Value1 = int(input())
    
    print("Enter  Number  2:")
    Value2 = int(input())
    
    print("Enter  Number  3:")
    Value3 = int(input())
    
    ret = Largest(Value1,Value2,Value3)
    
    print(f"Largest of the numbers is {ret}")
            
if __name__=="__main__":
    main()