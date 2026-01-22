# Write a program which accepts one number and prints cube of that number.

def NumCube(No):
    Cube = 1
    Cube = No ** 3
    return Cube

def main():
    No = int(input("Enter a number : "))

    Ret = NumCube(No)
    
    print(Ret)

if __name__ == "__main__":
    main()