import sys

def bfs(cost):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    max_cost = 0
    q = [(i, j) for i in range(N) for j in range(M)]
    #print('Q: ', q)
    while q:
        cur = q[0]
        q.pop(0)
        max_cost = max(max_cost, cost[cur[0]][cur[1]])
        for i in range(4):
            nxt = (cur[0] + dx[i], cur[1] + dy[i])
            if 0 <= nxt[0] and nxt[0] < N and 0 <= nxt[1] and nxt[1] < M:
                if cost[cur[0]][cur[1]] +1 < cost[nxt[0]][nxt[1]]:
                    cost[nxt[0]][nxt[1]] = cost[cur[0]][cur[1]] +1
                    q.append(nxt)
    return max_cost
    
def minimum_time(cost):
    ans = bfs(cost)
    low = 0
    high = ans-1
    while low <= high:
        mid = int(low + (high-low)/2)
        if possible(cost, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
    
def possible(cost, d):
    min_sum = min_dif = sys.maxsize
    max_sum = max_dif = -sys.maxsize - 1
    for i in range(N):
        for j in range(M):
            if cost[i][j] > d:
                max_sum = max(max_sum, i+j)
                min_sum = min(min_sum, i+j)
                max_dif = max(max_dif, i-j)
                min_dif = min(min_dif, i-j)
    for i in range(N):
        for j in range(M):
            cur = 0
            cur = max(cur, abs(max_sum - (i+j)))
            cur = max(cur, abs(min_sum - (i+j)))
            cur = max(cur, abs(max_dif - (i-j)))
            cur = max(cur, abs(min_dif - (i-j)))
            if cur <= d:
                return True
    return False

for T in range(int(input())):
    N, M = map(int, input().split())
    cost = []
    for i in range(N):
        cost.append(list(map(int, list(input()))))
    #print('Cost: ', cost)
    print(f'Case #{T+1}: {minimum_time(cost)}')