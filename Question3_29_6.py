""" The Smart Printer Queue (Priority Queue)"""

from collections import deque

class SmartPrinter:
    def __init__(self,max_len):
        self.urgent= deque(maxlen=max_len)
        self.normal= deque(maxlen=max_len)
        
    def add_job(self,job,priority="Normal"):
        if priority.upper()== "URGENT":
            self.urgent.append(job)
        else:
            self.normal.append(job)
            
    def print_job(self):
        if self.urgent:
            print("Printing Urgent :",self.urgent.popleft())
        elif self.normal:
            print("Printing Urgent :",self.normal.popleft())
        else :
            print("No job here ")
            
    def show_jobs(self):
        print("Urgent Jobs are :",list(self.urgent))
        print("Normal Jobs are :",list(self.normal))
        
        
sp=SmartPrinter(4)
sp.add_job("Document A")
sp.add_job("Invoice", "urgent")
sp.add_job("Report")
sp.add_job("Salary Slip", "urgent")

sp.show_jobs()

print("\nPrinting Jobs:")
sp.print_job()
sp.print_job()
sp.print_job()
sp.print_job()
sp.print_job()