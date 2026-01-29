# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18 

Mult = lambda No1,No2 : No1 * No2
    
def main():
    
    print("Enter  Number 1 :")
    No1 = int(input())
    
    print("Enter  Number 2 :")
    No2 = int(input())
    
    ret = Mult(No1,No2)
    print(f"Multiplication of numbers is {ret}")
            
if __name__=="__main__":
    main()