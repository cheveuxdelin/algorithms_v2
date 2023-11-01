class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        rtn = 0
        
        
        def f(x):
            visited[x] = True   
            for i in range(x, n):
                if visited[i] == False and isConnected[x][i] == 1:
                    f(i)
        
        for i in range(n):
            if visited[i] == False:
                rtn += 1
                f(i)
                
        return rtn
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [*range(n)]
        rank = [1] * n
        count = n

        def union(x1, x2):
            nonlocal count
            p1 = find(x1)
            p2 = find(x2)

            if p1 != p2:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                elif rank[p2] > rank[p1]:
                    parent[p1] = p2
                else:
                    parent[p1] = p2
                    rank[p2] += 1
                count -= 1

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for row in range(n):
            for col in range(row+1, n):
                if isConnected[row][col]:
                    union(row, col)
        return count