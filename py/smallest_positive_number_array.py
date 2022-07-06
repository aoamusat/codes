import json
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    a = sorted(A)
    n = len(a)
    low, high, ans = 0, n-1, 1
    while low <= high:
        mid = int(low + (high-low)/2)
        if a[mid] <= ans:
            if a[mid] == ans:
                ans += 1
                high = n-1
            low = mid+1
        else:
            high = mid-1
    return ans


file = open('/home/graco.silva/git/codes/inputs_outputs/entrada.in', 'r')
A = json.loads(file.read())
print(solution(A))
# file.write('[')
# for i in range(1,100000+1):
#     file.write(str(i)+",")
# file.write(']')
# file.close()