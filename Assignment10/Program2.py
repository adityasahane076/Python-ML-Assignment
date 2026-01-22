# Write a program which accepts one number and prints sum of first N numbers.

def SumNumbers(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i
    
    return Sum

def main():
    No = int(input("Enter a number : "))

    Ret = SumNumbers(No)

    print(Ret)
    
if __name__ == "__main__":
    main()