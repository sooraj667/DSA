#HASH TABLE
class Hashtable:
    def __init__(self):
        self.max=50
        self.arr=[[] for item in range(self.max)]
    
    def hashfunction(self,key):
        askival=0
        for item in key:
            askival+=ord(item)
        hashval=askival%self.max
        return hashval
    
    def add(self,key,value):
        hashval=self.hashfunction(key)
        found=0
        for index,item in enumerate(self.arr[hashval]):
            
            if item[0]==key:
                self.arr[hashval][index]=(key,value)
                found=1
            
                
        if found==0:
            self.arr[hashval].append((key,value))
            
        return self.arr

    def getitem(self,key):
        hashval=self.hashfunction(key)
        for item in self.arr[hashval]:
            if item[0]==key:
                return item[1]
        return "Not present"
    
    def delitem(self,key):
        hashval=self.hashfunction(key)
        for ind,element in enumerate(self.arr[hashval]):
            if element[0]==key:
                self.arr[hashval].pop(ind)
                return self.arr
        
        return ("Key not present")
                
        
    
#     def get(self,key):
#         hashval=self.hashfunction(key)
#         if self.arr[hashval]==None:
#             return ("Not present")
#         return self.arr[hashval]

        
    
    
        

    
h1=Hashtable()
h1.hashfunction("peno")
h1.add("open","Hello")
h1.add("openit","Hello Bro")
h1.add("peno","Bye")
h1.add("open","Sooraj")
h1.getitem('sdsd')
h1.delitem("peno")
# h1.add("aasas","Rx135")
# h1.get("asasas")