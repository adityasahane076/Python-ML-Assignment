# Write a program which accepts one number and prints that many numbers starting from 1.

def PrintNum(No):
    for i in range(1,No+1):
        print(i,end=" ")

def main():
    No = int(input("Enter first number : "))

    PrintNum(No)

if __name__ == "__main__":
    main()