# Question : Write a program which accepts one number and prints factorial of that number.

def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    
    return Fact

def main():
    No = int(input("Enter a number : "))

    Ret = Factorial(No)

    print(Ret)
    
if __name__ == "__main__":
    main()