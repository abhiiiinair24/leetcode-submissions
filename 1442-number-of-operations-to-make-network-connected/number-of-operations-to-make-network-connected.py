class Solution:
    def findParent(self,node,parent):

        if node == parent[node]:
            return node
        
        parent[node] = self.findParent(parent[node],parent)
        return parent[node]
    
    def UnionByRank(self,parent,rank,u,v):
        
        
        parentU = self.findParent(u,parent)
        parentV = self.findParent(v,parent)

        if parentU == parentV:
            return True

        if rank[parentU] > rank[parentV]:
            parent[parentV] = parentU
        elif rank[parentV] > rank[parentU]:
            parent[parentU] = parentV

        else:
            rank[parentU] +=1
            parent[parentV] = parentU

        return False
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        
        components = n
        if len(connections) < n-1:
            return -1
        
        parent = [i for i in range(n)]
        rank = [0]*n
        extracable = 0
        
        for u,v in connections:
            if self.UnionByRank(parent,rank,u,v) == True:
                extracable +=1
            else:
                components -=1
        
        if extracable >= components -1:
            return components-1
        else:
            return -1
        



