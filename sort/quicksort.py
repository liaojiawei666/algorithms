import random
def partition(A, p, r):
    if p < r:
        tmp = A[r]
        left, right = p, r
        while left < right:
            while left < right and A[left] <= tmp:
                left += 1
            A[right] = A[left]
            while left < right and A[right] >= tmp:
                right -= 1
            A[left] = A[right]
        A[left] = tmp
        return left


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
    return A

def test():
    x=[random.randint(0,100) for i in range(20)]
    quicksort(x,0,len(x)-1)
    print(x)
test()