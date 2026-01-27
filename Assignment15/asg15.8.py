# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
# divisible by both 3 and 5.

def main():
    
    Data = [2,3,45,30,6,15,8,9]
    
    FData = list(filter(lambda No : ((No % 3 == 0) and (No % 5 == 0)),Data))
    
    print("The Filtered list even number is : ",FData)
    
if __name__ == "__main__":
    main()