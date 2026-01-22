# Write a program which accepts one number and prints binary equivalent.

def PrintBinary(No):
    Binary = bin(No)

    print(Binary)

def main():
    No = int(input("Enter number : "))

    PrintBinary(No)

if __name__ == "__main__":
    main()