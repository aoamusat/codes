g = [[1, 3], [0, 3], [3], []]
n = len(g)
visited = [False]*n
components = [-1]*n
count = 0

def find_components():
	global count
	for i in range(n):
		if not visited[i]:
			count += 1
			dfs(i)
	return (count, components)

def dfs(at):
	visited[at] = True
	components[at] = count
	for node in g[at]:
		if not visited[node]:
			dfs(node)

print(find_components())