class Stack:
    def __init__(self):
        self.stack=[]
    
    
    def pushit(self,data):
        self.stack.append(data)
        
    def popit(self):
        self.stack.pop()
    
    def trav(self):
        for item in self.stack:
            print(item)
        
s1=Stack()
s1.pushit(11)
s1.pushit(22)
s1.pushit(33)
s1.pushit(44)
s1.popit()
s1.trav()