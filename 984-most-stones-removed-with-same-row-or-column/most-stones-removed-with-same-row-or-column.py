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
        n = len(stones)

        parent = [i for i in range(n)]
        size = [1] * n

        rowMap = {}
        colMap = {}

        for stoneIndex, (row, col) in enumerate(stones):

            if row in rowMap:
                previousStone = rowMap[row]
                self.unionBySize(
                    stoneIndex, previousStone, parent, size
                )
            else:
                rowMap[row] = stoneIndex

            if col in colMap:
                previousStone = colMap[col]
                self.unionBySize(
                    stoneIndex, previousStone, parent, size
                )
            else:
                colMap[col] = stoneIndex

        components = 0

        for stoneIndex in range(n):
            if self.findParent(stoneIndex, parent) == stoneIndex:
                components += 1

        return n - components