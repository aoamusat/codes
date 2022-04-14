
def countImbalance(weights, k):
    n = len(weights)
    count = 0
    for i in range(n):
        min_weight = max_weight = weights[i]
        for j in range(i, n):
            min_weight = min(weights[j], min_weight)
            max_weight = max(weights[j], max_weight)
            if max_weight - min_weight <= k:
                count += 1

    return count

weights = [1, 2, 3, 4]
k = 3
print(countImbalance(weights, k))
