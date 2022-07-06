def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    i=0
    for c in t:
        if i < len(s):
            if s[i] == c:
                i += 1
    return i == len(s)

s = 'ace'
t = 'abcde'
print(isSubsequence(s, t))