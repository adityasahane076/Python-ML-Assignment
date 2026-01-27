# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
# numbers.

def main():
    
    Data = [2,3,45,30,6,15,8,9]
    
    FData = list(filter(lambda No : (No % 2 == 0),Data))
    
    print("The Filtered list even number is : ",len(FData))
    
if __name__ == "__main__":
    main()