# 1: Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

import threading

def DisplayEven():
    print("DisplayEven function Thread ID : ",threading.get_ident())
    
    for i in range(2,21,2):
        print(i,end="\t")

    print() 
    
def DisplayOdd():
    print("DisplayOdd function Thread ID : ",threading.get_ident())

    for i in range(1,20,2):
        print(i,end="\t")

    print() 
        
def main():
    
    print("Main function Thread ID : ",threading.get_ident())

    t1 = threading.Thread(target=DisplayEven)
    t1.start()

    t2 = threading.Thread(target=DisplayOdd)
    t2.start()
        
    t1.join()
    t2.join()
    
if __name__ == "__main__":
    main()