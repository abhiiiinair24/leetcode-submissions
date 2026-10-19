class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:

        heap = []
        n = len(grid)
        m = len(grid[0])
        visited = [[False] *m for _ in range(n)]
        print(visited)

        heapq.heappush(heap,(grid[0][0],0,0))

        drow = [0,-1,0,1]
        dcol = [-1,0,1,0]

        while heap:

            currtime,currRow,currCol = heapq.heappop(heap)

            if visited[currRow][currCol]:
                continue

            #print("Entering heap")
            if not visited[currRow][currCol]:
                visited[currRow][currCol] = True
                print("Mark: ",currRow,currCol)
            
            if currRow == n-1 and currCol == m-1:
                return currtime
            for i in range(4):
                nrow = drow[i]+currRow
                ncol = dcol[i] +currCol
            
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] == False:
                    nexttime = max(currtime,grid[nrow][ncol])
                    heapq.heappush(heap,(nexttime,nrow,ncol))
                
                

        

        