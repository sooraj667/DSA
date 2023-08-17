

# # ADJACENCY MATRIX
# nodes=[]
# graph=[]


# def addnode(value):
#     nodes.append(value)
#     if graph==[]:
#         graph.append([0])
#     else:
#         for item in graph:
#             item.append(0)
#         temp=[]
#         for i in range(len(nodes)):
#             temp.append(0)

#         graph.append(temp)


# def addedge(n1,n2):
#     if n1 not in nodes:
#         print("Nodes  not present")
#         return
#     if n2 not in nodes:
#         print("Nodes  not present")
#         return
    
         
#     index1=nodes.index(n1)
#     index2=nodes.index(n2)
#     graph[index1][index2]=1
#     graph[index2][index1]=1


# def trav():
#     for i in range(len(nodes)):
#         for j in range(len(nodes)):
#             print(graph[i][j] ,end=" ")

#         print()

# def deletenode(n1):
#     index=nodes.index(n1)
#     nodes.pop(index)

#     graph.pop(index)
#     for item in graph:
#         item.pop(index)

# def deleteedge(n1,n2):
#     if n1 not in nodes:
#         print("Node not presnet")
        
#     elif n2 not in nodes:
#         print('Node not present')

#     else:
#         ind1=nodes.index(n1)
#         ind2=nodes.index(n2)

#         graph[ind1][ind2]=0
#         graph[ind2][ind1]=0



    










# addnode("A")
# addnode("B")
# addnode("C")
# addnode("D")
# addnode("E")
# # trav()
# addedge("A","B")
# addedge("C","E")
# print(nodes)
# # deletenode("E")
# # deletenode("A")
# deleteedge("A","B")


# trav()



# ADJACENCY LIST

class Adjlist:
    def __init__(self):
        self.graph={}
        self.visited=[]

    def addnode(self,value):
        if value not in self.graph:
            self.graph[value]=[]
        else:
            print(f"{value} already present!")

    
    def addedge(self,n1,n2):
        if n1 not in self.graph:
            print(f"{n1} not in the graph" )
            return
        if n2 not in self.graph:
            print(f"{n2} not in the graph" )
            return
        
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)


    def deletenode(self,value):
        temp=[]
        for item in self.graph[value]:
            temp.append(item[0])
        self.graph.pop(value)
        for item in temp:
            for tup in self.graph[item]:
                if tup[0]==value:
                    self.graph[item].remove(tup)

    def deleteedge(self,n1,n2):
        for tup in self.graph[n1]:
            if tup[0]==n2:
                self.graph[n1].remove(tup)
                
        for tup in self.graph[n2]:
            if tup[0]==n1:
                self.graph[n2].remove(tup)


    def DFSrecursion(self,node):
        if node not in self.graph:
            print("Node not present")
            return
        
        if node not in self.visited:
            print(node)
            self.visited.append(node)
            for i in self.graph[node]:
                self.DFSrecursion(i)

    def DFSstackmethod(self,node):
        visitedlist=[]
        stack=[]
        if node not in self.graph:
            print("Node not present")
            return
        stack.append(node)
        while stack:
            current=stack.pop()
            if current not in visitedlist:
                print(current)
                visitedlist.append(current)
                for i in self.graph[current]:
                    stack.append(i)
        
        


            






visited=[]
a=Adjlist()



a.addnode("A")
a.addnode("B")
a.addnode("C")
a.addnode("D")
a.addedge("A","B")
a.addedge("A","C")
a.addedge("A","D")

# a.deletenode("B")
# a.deleteedge("A","B")
print(a.graph)
# a.DFSrecursion("A")
a.DFSstackmethod("A")

