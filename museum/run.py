from multiprocessing import Process
import os

def run_app1():
    os.system("py menu.py")

def run_app2():
    os.system("py basic_tkt.py")

def run_app3():
    os.system("py combo_tkt.py") 
    
def run_app4():
    os.system("py drama_tkt.py")
    
def run_app5():
    os.system("py jewellery.py")
    
def run_app6():
    os.system("py library_book_entry.py")
    
def run_app7():
    os.system("py library_book_issue.py")
    
def run_app8():
    os.system("py library_cd_issue.py")

def run_app9():
    os.system("py library_cds_entry.py")
    
def run_app10():
    os.system("py library_lost_book.py")

def run_app11():
    os.system("py library_lost_cd.py")
    
def run_app12():
    os.system("py library_membership.py")
    
def run_app13():
    os.system("py museum_exhibition.py")

def run_app14():
    os.system("py museum_master.py")
    
def run_app15():
    os.system("py museum_membership.py")
    
def run_app16():
    os.system("py pottery.py")
    
def run_app17():
    os.system("py sculpture.py")

def run_app18():
    os.system("py stone.py")

def run_app19():
    os.system("py textiles.py")

def run_app20():
    os.system("py login.py")



if __name__ == "__main__":
    p1 = Process(target=run_app1)
    p2 = Process(target=run_app2)
    p3 = Process(target=run_app3)
    p4 = Process(target=run_app4)
    p5 = Process(target=run_app5)
    p6 = Process(target=run_app6)
    p7 = Process(target=run_app7)
    p8 = Process(target=run_app8)
    p9 = Process(target=run_app9)
    p10 = Process(target=run_app10)
    p11 = Process(target=run_app11)
    p12 = Process(target=run_app12)
    p13 = Process(target=run_app13)
    p14 = Process(target=run_app14)
    p15 = Process(target=run_app15)
    p16 = Process(target=run_app16)
    p17 = Process(target=run_app17)
    p18 = Process(target=run_app18)
    p19 = Process(target=run_app19)
    p20 = Process(target=run_app20) 
   
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()
    p17.start()
    p18.start()
    p19.start()
    p20.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()
    p17.join()
    p18.join()
    p19.join()
    p20.join()
    