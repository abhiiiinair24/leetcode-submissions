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
            return 

        if rank[parentU] > rank[parentV]:
            parent[parentV] = parentU
        elif rank[parentV] > rank[parentU]:
            parent[parentU] = parentV

        else:
            rank[parentU] +=1
            parent[parentV] = parentU

        return
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        hashmap ={}
        parent = [i for i in range(n)]
        rank = [0]*n

        for i in range(n):
            for email in accounts[i][1:]:
                if email not in hashmap:
                    hashmap[email] =i
                else:
                    previousRow = hashmap[email]
                    self.UnionByRank(parent,rank,previousRow,i)
        


        print("Parent: ",parent)
        print("Rank: ",rank)
        print("Hashmap: ",hashmap)

        #Merging
        mergedaccount = [[] for _ in range(n)]
        print(mergedaccount)

        for email,row in hashmap.items():
            ultimateParent = self.findParent(row,parent)
            mergedaccount[ultimateParent].append(email)
        
        answer = []
        for i in range(n):
            if mergedaccount[i]:
                mergedaccount[i].sort()
                val = mergedaccount[i]
                currentAccount = [accounts[i][0]] + val #[accounts[i][0]]#making this list
                print(currentAccount)
                answer.append(currentAccount)
        print(answer)

        return answer