
def countVoteGroups(related):
    visited = [False] * len(related)
    count = 0
    for i in range(len(related)):
        for j in range(len(related)):
            if (i != j and related[i][j] == '1' and not visited[j] and not visited[i]) or (i == j and not visited[j]):
                visited[j] = True
                count += 1
            elif i != j and related[i][j] == '1' and  visited[j]:
                break
        visited[i] = True
    return count

related = ['1100', '1110', '0110', '0001']
print(countVoteGroups(related))