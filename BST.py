# BINARY SEARCH TREE

class BST:
    def __init__(self,key=None):
        self.key=key
        self.lchild=None
        self.rchild=None
        
        
    
    
    def insert(self,data):
        if self.key==None:
            self.key=data
            return
        
        if self.key==data:
            print("Duplicates not allowed")
            return
        
        
        if data<self.key:
            if self.lchild!=None:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
                
                
        else:
            if self.rchild!=None:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)
                
    def search(self,data):
        if self.key==data:
            print("DATA FOUND!")
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Data NOT found")
        
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Data NOT found")
                
        
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)
       
    def delete(self,data):
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data)
            else:
                print("Data not present")
        
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print("Data Not present")
        
        else:
            if self.lchild==None:
                temp=self.rchild
                self=None
                return temp
            elif self.rchild==None:
                temp=self.lchild
                self=None
                return temp
            else:
                node=self.rchild
                while self.lchild!=None:
                    node=node.lchild
                    
                self.key=node.key
                self.rchild=self.rchild.delete(node.key)
        return self
            
    def minval(self):
       
        while self.lchild !=None:
            self=self.lchild
            
        print(f"Smallest value is {self.key}")
    
    def maxval(self):
        while self.rchild !=None:
            self=self.rchild
            
        print(f"Largest value is {self.key}")
        
        
    
    
b1=BST(10)
b1.insert(100)
b1.insert(34)
b1.insert(2)
b1.insert(99)
# b1.preorder()
# b1.search(4)
# b1.inorder()
# b1.postorder()
b1.delete(1)
b1.minval()
b1.maxval()
b1.inorder()
