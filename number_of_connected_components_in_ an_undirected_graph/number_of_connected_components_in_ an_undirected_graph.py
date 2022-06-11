class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        al = collections.defaultdict(list)

        # adjacency list , stores all connected nodes to respective node
        for x,y in edges:
            al[x].append(y)
            al[y].append(x) 
            
        connected_components = 0
        visited = set()            

        def dfs(node):
            if node not in visited:
                visited.add(node)
            else:
                return

            for x in al[node]:
                dfs(x)

        for node in range(n):
            if node not in visited:
                dfs(node)
                connected_components += 1

        return connected_components