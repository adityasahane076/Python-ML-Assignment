# Write a program which accepts one number and prints square of that number.

def NumSquare(No):
    Sq = 1
    Sq = No * No
    return Sq

def main():
    No = int(input("Enter a number :"))

    Ret = NumSquare(No)
    
    print(Ret)

if __name__ == "__main__":
    main()