class Solution:
    def findParent(self,node, parent):
        if node == parent[node]:
            return node
        
        parent[node] = self.findParent(parent[node],parent)
        
        return parent[node]
    def Unionbysize(self,u,v,parent,size):

        pu = self.findParent(u,parent)
        pv = self.findParent(v,parent)

        if pu == pv:
            return False
        if size[pu] < size[pv]:
            size[pv] += size[pu]
            parent[pu] = pv
        else:
            size[pu] += size[pv]
            parent[pv] = pu

        return True
    def largestIsland(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        parent = [i for i in range(n*n)]
        size = [1]*(n*n)

        # print(parent)
        # print(size)

        drow = [0,-1,0,1]
        dcol = [-1,0,1,0]

        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    node = i*n + j
                    # print(node)

                    for k in range(4):
                        nrow = drow[k] + i
                        ncol = dcol[k] + j
                        
                        if nrow >= 0 and nrow < n and ncol >=0 and ncol < n and grid[nrow][ncol] == 1:
                            neinode = nrow*n + ncol
                            # print(neinode)
                            self.Unionbysize(node,neinode,parent,size)
        

        # print('Parent: ',parent)
        # print('Size: ',size)
        maxvalue = float('-inf')
        zerocheck = False
      #  print(maxvalue)
       # zeronode = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    zerocheck = True
                    uniqueset = set()
                    for k in range(4):
                        nrow = drow[k] + i
                        ncol = dcol[k] + j
                        if nrow >=0 and nrow < n and ncol >= 0 and ncol < n and grid[nrow][ncol] == 1:    
                            neinode = nrow * n + ncol
                            ultimateparent = self.findParent(neinode,parent)
                            uniqueset.add(ultimateparent)

                    # print(uniqueset)
                    possiblesize = 1
                    for ultimateParent in uniqueset:
                        possiblesize += size[ultimateParent]
                    
                    # print(possiblesize)
                    maxvalue = max(maxvalue, possiblesize)
        
        if zerocheck == False:
            return n*n
        
        return maxvalue
        
