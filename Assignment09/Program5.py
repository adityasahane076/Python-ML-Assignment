# Write a program which accepts one number and check whether it is divisible by 3 and 5.

def ChkDivisble(No):
    if ((No % 3 == 0)&(No % 5 == 0)):
        return True
    else:
        return False

def main():
    No = int(input("Enter a number : "))

    Ret = ChkDivisble(No)
    
    if Ret == True :
        print("Divisible by 3 and 5 both")
    else:
        print("not divisible by 3 or 5 or both")

if __name__ == "__main__":
    main()