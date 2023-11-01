class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [*range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n: int) -> int:
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]

        def union(u: int, v: int) -> bool:
            p1, p2 = find(u), find(v)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]