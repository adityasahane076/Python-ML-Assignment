# Write a program which accepts marks and displays grade.

def DispGrade(Marks):
    if (Marks < 0 or Marks > 100):
        print("Invalid")
        return

    if (Marks >= 75):
        print("Distinction")
    elif (Marks >= 60):
        print("First Class")
    elif (Marks >= 50):
        print("Second Class")
    elif (Marks < 50):
        print("Fail")
    

def main():
    Marks = int(input("Enter number : "))

    DispGrade(Marks)

if __name__ == "__main__":
    main()