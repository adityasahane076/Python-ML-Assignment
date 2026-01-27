#10. Write a program which accept name from user and display length of its name.
# Input : Marvellous Output : 10 

def fun(str):
    return len(str)
        
def main():
    
    print("Enter String")
    str = input()
    ret = fun(str)  
    
    print(f" length of |{str}| is {ret}")  
    
if __name__=="__main__":
    main()