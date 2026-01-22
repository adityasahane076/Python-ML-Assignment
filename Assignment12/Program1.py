#Write a program which accepts one character and checks whether it is vowel or consonant.

def CheckChar(ch):
    if (ch == "a" or ch == "e" or ch == 'i' or ch == "o" or ch == "u"):
        print("It is vowel")
    else:
        print("It is consonant")

def main():
    ch = input("Enter character : ")[0]

    CheckChar(ch)

if __name__ == "__main__":
    main()