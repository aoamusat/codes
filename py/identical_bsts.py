# A Python3 program to check for Identical
# BSTs without building the trees
 
# # The main function that checks if two
# arrays a[] and b[] of size n construct
# same BST. The two values 'min' and 'max'
# decide whether the call is made for left
# subtree or right subtree of a parent
# element. The indexes i1 and i2 are the
# indexes in (a[] and b[]) after which we
# search the left or right child. Initially,
# the call is made for INT_MIN and INT_MAX
# as 'min' and 'max' respectively, because
# root has no parent. i1 and i2 are just
# after the indexes of the parent element in a[] and b[]. */

def util(a, b, n, i1, i2, min, max):
    # # Search for a value satisfying the
    # constraints of min and max in a[] and
    # b[]. If the parent element is a leaf
    # node then there must be some elements
    # in a[] and b[] satisfying constraint. */
    j, k = i1, i2
    while j < n:
        if (a[j] > min and a[j] < max):
            break
        j += 1
    while k<n:
        if (b[k] > min and b[k] < max):
            break
        k += 1
 
    # If the parent element is leaf in both arrays */
    if (j == n and k == n):
        return True
 
    # Return false if any of the following is true
        # a) If the parent element is leaf in one array,
        #     but non-leaf in other.
        # b) The elements satisfying constraints are
        #     not same. We either search for left
        #     child or right child of the parent
        #     element (decided by min and max values).
        #     The child found must be same in both arrays */
    if (((j == n) ^ (k == n)) or a[j] != b[k]):
        return False
 
    # Make the current child as parent and
    # recursively check for left and right
    # subtrees of it. Note that we can also
    # pass a[k] in place of a[j] as they
    # are both are same */
    print('a[j]:', a[j], 'min:',min,'max:', max)
    return util(a, b, n, j + 1, k + 1, a[j], max) and util(a, b, n, j + 1, k + 1, min, a[j]) #Left Subtree


def solution(arrayOne, arrayTwo):
    # write your code here
    n = len(arrayOne)
    return util(arrayOne, arrayTwo, n, 0, 0, -10**9, 10**9)
    
if __name__ == '__main__':
    a = [2, 4, 3, 1]
    b = [2, 1, 4, 3]
    n = len(a)
 
    if(solution(a, b)):
        print("BSTs are same")
    else:
        print("BSTs not same")