# Write a program which accepts radius of circle and prints area of circle.

def CalculateArea(radius):
    Area = 3.14 * radius *radius

    return Area

def main():
    radius = int(input("Enter radius : "))

    Ret = CalculateArea(radius)

    print("Area of circle is : ",Ret)


if __name__ == "__main__":
    main()