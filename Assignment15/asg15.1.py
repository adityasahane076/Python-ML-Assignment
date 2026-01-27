# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of
# each number.

def main():
    
    Data = [2,3,4,5,6,7,8,9]
    
    MData = list(map(lambda No : No*No,Data))
    
    print("After mapping list is : ",MData)
if __name__ == "__main__":
    main()