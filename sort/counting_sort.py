# 计数排序
import random


def counting_sort(A, B, k):
    C = [0 for i in range(k+1)]
    for x in A:
        C[x] += 1
    C[0] -= 1
    for i in range(len(C) - 1):
        C[i + 1] += C[i]
    for x in A:
        B[C[x]] = x
        C[x] -= 1

#测试###########################################
A = [random.randint(0, 100) for i in range(100)]
B = [-1 for i in range(100)]
counting_sort(A, B, 100)
print(B)
#################################################
