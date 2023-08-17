class Queue:

    def __init__(self):
        self.queue=[]
    
    
    def enqueue(self,data):
        self.queue.append(data)
        
    def dequeue(self):
        self.queue.pop(0)
        
    def trav(self):
        for item in self.queue:
            print(item)
    
q=Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
q.enqueue(400)
q.dequeue()
q.trav()