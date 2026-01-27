# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd
# numbers

def main():
    
    Data = [2,3,4,5,6,7,8,9]
    
    FData = list(filter(lambda No : (No % 2 == 1),Data))
    
    print("The Filtered list of odd number is : ",FData)
if __name__ == "__main__":
    main()