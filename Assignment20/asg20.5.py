#5: Design a Python application that creates two threads named Thread1 and Thread2.
# • Thread1 should display numbers from 1 to 50.
# • Thread2 should display numbers from 50 to 1 in reverse order.
# • Ensure that:
# ◦ Thread2 starts execution only after Thread1 has completed.
# • Use appropriate thread synchronizatio

import threading

def Display():
    print("Display function Thread ID : ",threading.get_ident())
    
    for i in range(1,51,1):
        print(i,end="\t")
            
    print()
    
def DisplayRev():
    print("DisplayRev function Thread ID : ",threading.get_ident())

    for i in range(50,0,-1):
        print(i,end="\t")
            
    print()
        
def main():
    
    print("Main function Thread ID : ",threading.get_ident())

    Thread1 = threading.Thread(target=Display)
    Thread1.start()
    
    Thread2 = threading.Thread(target=DisplayRev)
    Thread2.start()
        
    # Thread1.join()
    # Thread2.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()