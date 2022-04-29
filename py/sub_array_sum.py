def subArraySum(arr, n, s): 
    #Write your code here7
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > s and start < i-1:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == s:
            return [start+1, i]
        if i < n:
            curr_sum += arr[i]
        i += 1
    return [-1]

arr1 = [135,101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134]
arr2 = [1,2,3,7,5]
arr3 = [1,2,3,4,5,6,7,8,9,10]
arr4 = [28,68,142,130,41,14,175,2,78,16,84,14,193,25,2,193,160,71,29,28,85,76,187,99,171,88,48,5,104,22,64,107,164,11,172,90,41,165,143,20,114,192,105,19,33,151,6,176,140,104,23,99,48,185,49,172,65]
print(subArraySum(arr1, 42, 468))
print(subArraySum(arr2, 5, 12))
print(subArraySum(arr3, 10, 15))
print(subArraySum(arr4, 57, 1562))