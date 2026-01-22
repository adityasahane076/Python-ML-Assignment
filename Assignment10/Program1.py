# Write a program which accepts one number and prints multiplication table of that number.

def MulTable(No):
    Mult = 0
    for i in range(1,11):
        Mult = i * No
        print(Mult,end=" ")

def main():
    No = int(input("Enter a number : "))

    MulTable(No)
    
if __name__ == "__main__":
    main()