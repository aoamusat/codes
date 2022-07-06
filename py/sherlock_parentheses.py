T = int(input())
for i in range(T):
    l, r = map(int, input().split())
    n = min(l, r)
    print(f"Case #{i+1}: {int(n*(n+1)/2)}")