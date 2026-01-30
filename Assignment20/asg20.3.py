# 3: Design a Python application that creates two threads named EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading

def EvenList(list):
    print("EvenFactors function Thread ID : ",threading.get_ident())
    
    Sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            Sum = Sum + list[i]
            

    print("Sum of Even Elements of list is : ",Sum) 
    
def OddList(list):
    print("OddFactors function Thread ID : ",threading.get_ident())

    Sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 1:
            Sum = Sum + list[i]
            


    print("Sum of Odd Elements of list  is : ",Sum) 
        
def main():
    
    print("Main function Thread ID : ",threading.get_ident())
    
    Data = [1,2,3,4,5,6,7,8,9,10]
    
    t1 = threading.Thread(target=EvenList,args=(Data,))
    t1.start()

    t2 = threading.Thread(target=OddList,args=(Data,))
    t2.start()
        
    t1.join()
    t2.join()
    
    print("Exit from main")
    
if __name__ == "__main__":
    main()