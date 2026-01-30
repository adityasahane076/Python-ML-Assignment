# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.
# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
# ◦ Identify all even factors of the given number.
# ◦ Calculate and display the sum of even factors.
# • The OddFactor thread should:
# ◦ Identify all odd factors of the given number.
# ◦ Calculate and display the sum of odd factors.
# • After both threads complete execution, the main thread should display the message:  “Exit from main”

import threading

def EvenFactors(No):
    print("EvenFactors function Thread ID : ",threading.get_ident())
    
    Sum = 0
    for i in range(2,(No//2) + 1,2):
        if No % i == 0:
            Sum = Sum + i
            

    print("Sum of Even Factors is : ",Sum) 
    
def OddFactors(No):
    print("OddFactors function Thread ID : ",threading.get_ident())

    Sum = 0
    for i in range(1,(No//2) + 1,2):
        if No % i == 0:
            Sum = Sum + i

    print("Sum of Odd Factors is : ",Sum) 
        
def main():
    
    print("Main function Thread ID : ",threading.get_ident())

    t1 = threading.Thread(target=EvenFactors,args=(15,))
    t1.start()

    t2 = threading.Thread(target=OddFactors,args=(15,))
    t2.start()
        
    t1.join()
    t2.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()