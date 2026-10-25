class Solution:
    def findParent(self, node, parent):
        if parent[node] == node:
            return node

        parent[node] = self.findParent(parent[node], parent)
        return parent[node]

    def unionBySize(self, u, v, parent, size):
        parentU = self.findParent(u, parent)
        parentV = self.findParent(v, parent)

        if parentU == parentV:
            return

        if size[parentU] < size[parentV]:
            parent[parentU] = parentV
            size[parentV] += size[parentU]
        else:
            parent[parentV] = parentU
            size[parentU] += size[parentV]

    def removeStones(self, stones: list[list[int]]) -> int:

        n  = len(stones)

        parent = [i for i in range(n)]
        size = [1]* n

        rowmap ={}
        colmap = {}

        for stoneind, (row,col) in enumerate(stones):
            if row in rowmap:
                previousRow = rowmap[row]
                self.unionBySize(previousRow,stoneind,parent,size)

            else:
                rowmap[row] = stoneind
            
            if col in colmap:
                previousCol = colmap[col]
                self.unionBySize(previousCol,stoneind,parent,size)
            else:
                colmap[col] = stoneind
        
        cnt = 0
        for stoneind in range(n):
            if self.findParent(stoneind,parent) == stoneind:
                cnt +=1

        return n - cnt

   