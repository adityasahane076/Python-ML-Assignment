# 4: Design a Python application that creates three threads named Small, Capital, and Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# ◦ Thread ID
# ◦ Thread Name

import threading

def LowerCase(str):
    print("LowerCase function Thread ID : ",threading.get_ident())
    print("Name of thread is : ",threading.current_thread().name)
    
    Count = 0
    for i in range(len(str)):
        if str[i] >= "a" and str[i] <= "z":
            Count = Count + 1   


    print("Number of lowercase characters are : ",Count) 
    
def UpperCase(str):
    print("UpperCase function Thread ID : ",threading.get_ident())
    print("Name of thread is : ",threading.current_thread().name)

    Count = 0
    for i in range(len(str)):
        if str[i] >= "A" and str[i] <= "Z":
            Count = Count + 1   


    print("Number of uppercase characters are : ",Count)
            
def Numeric(str):
    print("Numeric function Thread ID : ",threading.get_ident())
    print("Name of thread is : ",threading.current_thread().name)

    Count = 0
    for i in range(len(str)):
        if str[i] >= "0" and str[i] <= "9":
            Count = Count + 1   


    print("Number of numeric digit are : ",Count) 
        
def main():
    
    print("Main function Thread ID : ",threading.get_ident())
    print("Name of thread is : ",threading.current_thread().name)
    
    t1 = threading.Thread(target=LowerCase,args=("Data112",))

    t2 = threading.Thread(target=UpperCase,args=("Data112",))
        
    t3 = threading.Thread(target=Numeric,args=("Date112",))
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()