for case in range(int(input())):
    N, Q = map(int, input().split())
    seen = [None]*(N+1)
    act = [0]*26
    seen[0] = tuple(act)
    for i, ch in enumerate(input().strip()):
        act[ord(ch)-ord('A')] += 1
        seen[i+1] = tuple(act)
    res = 0
    for _ in range(Q):
        L, R = map(int, input().split())
        fr, to = seen[L-1], seen[R]
        if sum((to[j]-fr[j]) % 2 for j in range(26)) <= 1:
            res += 1
    print(f'Case #{case+1}: {res}')

