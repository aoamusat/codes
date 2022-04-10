g = [[1,2, 3], [0, 3, 2]]
n = max(max(g))+1
visited = [False]*n

def dfs(at):
	if visited[at]: return
	visited[at] = True

	neighbours = g[at]
	for node in neighbours:
		dfs(node)

start_node = 0
dfs(start_node)