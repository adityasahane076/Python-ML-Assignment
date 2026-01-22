# Write a program which accepts one number and prints reverse of digits.

def Reverse(No):
    Rev = 0
    while(No > 0):
        Rem = No % 10
        Rev = Rev * 10 + Rem
        No = No // 10

    return Rev

def main():
    No = int(input("Enter a number : "))

    Ret = Reverse(No)

    print(Ret)
    
if __name__ == "__main__":
    main()