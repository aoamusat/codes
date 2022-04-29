def candyStore(candies,N,K):
    # code here
    sorted_candies = sorted(candies)
    min_cost = max_cost = 0
    size = 0
    if K > 0:
        size = N // (K+1)
        if N % (K+1) != 0:
            size += 1
    else:
        size = N
    for i in range(size):
        min_cost += sorted_candies[i]
    i = N-1
    for j in range(size):
        max_cost += sorted_candies[i]
        i -= 1
    return min_cost, max_cost


input1 = ([3,2,1,4], 4, 2) # 1,2,3,4
input2 = ([1,2,3,4,5,6,7,8,9,10], 10, 1)
input3 = ([1,2,3,4,5,6,7,8,9,10], 10, 2)
print(candyStore(*input1))
print(candyStore(*input2))
print(candyStore(*input3))
