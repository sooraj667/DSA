class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        
    def trav(self):
        if self.head==None:
            print("The Linked List is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.ref
                
    def addatbeg(self,data):
        nodeobj=Node(data)
        if self.head==None:
            self.head=nodeobj
        else:
            
            nodeobj.ref=self.head
            self.head=nodeobj
    
    def addatend(self,data):
        nodeobj= Node(data)
        if self.head == None:
            self.head=nodeobj
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=nodeobj
            
        
    def search(self,data):
        n=self.head
        while n!=None:
            if n.data==data:
                print(f"Data found! --> {data}")
                return
            else:
                n=n.ref
                
            
        print(f"{data} not found!")
        return
            
    def deletefromend(self):
        if self.head ==None:
            print("Empty LL")
            return
        
        
        n=self.head
        while n.ref.ref!=None:
            n=n.ref
        
        n.ref=None
        return
    
    def deletefrombeg(self):
        if self.head ==None:
            print("Empty LL")
            return
        
        self.head=self.head.ref
        return

    def insertbef(self,value,data):
        if self.head ==None:
            print("Empty LL")
            return
        nodeobj=Node(value)
        n=self.head
        while n.ref!=None:
            if n.ref.data==data:
                nodeobj.ref=n.ref
                n.ref=nodeobj
                return
            else:
                n=n.ref
        print("Data Not Found")
    
    def insertafter(self,value,data):
        if self.head ==None:
            print("Empty LL")
            return
        nodeobj=Node(value)
        n=self.head
        while n!=None:
            if n.data==data:
                nodeobj.ref=n.ref
                n.ref=nodeobj
                return
            else:
                n=n.ref
        print(f"{data} not in this list")
            
        
    def deleteelement(self,data):
        if self.head ==None:
            print("Empty LL")
            return
        n=self.head
        while n.ref!=None:
            if n.ref.data==data:
                n.ref=n.ref.ref
                return
            else:
                n=n.ref
        
        print("Data Not found!")
        
        
        
                
            
        

        
linkobj=LinkedList()

linkobj.addatend(100)
linkobj.addatend(200)
linkobj.addatend(44)
linkobj.addatbeg(1)
linkobj.addatbeg(4)


linkobj.deletefromend()
linkobj.deletefromend()
linkobj.deletefrombeg()
linkobj.insertbef(3000,45)
linkobj.insertafter(3000,2)
linkobj.deleteelement(100)
linkobj.deleteelement(200)
linkobj.deleteelement(200)
linkobj.insertbef(value=30,data=300)
linkobj.trav()
        