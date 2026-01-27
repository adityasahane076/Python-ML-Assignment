# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings
# having length greater than 5

def main():
    
    Data = ["aditya","rushikesh","affan","abhijeet","vaibhav","aarjav","utkarsh","sumit"]
    
    FData = list(filter(lambda str : (len(str) > 5),Data))
    
    print("The String with length greater than 5 is : ",FData)
if __name__ == "__main__":
    main()