#8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5 Output : * * * * * 

def fun(No):
    for i in range(No):
        print("*",end="\t")
        
def main():
    
    print("Enter Number")
    No = int(input())
    fun(No)    
    
if __name__=="__main__":
    main()