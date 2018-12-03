import random


def kth(A, l, r, k):
    if l == r:
        return A[l]
    elif l < r:
        p = partition(A, l, r)
        offset = p - l + 1
        if offset == k:
            return A[p]
        elif offset < k:
            return kth(A, p + 1, r, k - offset)
        else:
            return kth(A, l, p - 1, k)


def partition(A, l, r):
    tmp = A[r]
    left, right = l, r
    while left < right:
        while left < right and A[left] <= tmp:
            left += 1
        A[right] = A[left]
        while left < right and A[right] >= tmp:
            right -= 1
        A[left] = A[right]
    A[left] = tmp
    return left


x = [random.randint(1, 100) for i in range(10)]
print(x)
y = kth(x, 0, len(x) - 1, 2)
print(y)
