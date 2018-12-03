import random
def max_heapifa(A, i):
    #维护堆函数
    A_len = len(A)
    while (i < A_len):
        l = 2 * i
        r = 2 * i + 1
        if l < A_len and A[i] < A[l]:
            largest = l
        else:
            largest = i
        if r < A_len and A[largest] < A[r]:
            largest = r
        if largest != i:
            temp = A[i]
            A[i] = A[largest]
            A[largest] = temp
            i = largest
        else:
            break


def build_max_heap(A):
    #建立第一个堆
    A_heap_size=len(A)
    for i in range((A_heap_size-1)//2,-1,-1):
        max_heapifa(A,i)

def heap_sort(A):
    B=[]
    build_max_heap(A)
    while(len(A)>1):
        B.append(A[0])
        A[0]=A.pop()
        max_heapifa(A,0)
    B.append(A[0])
    return B
#
# def test():
#     #测试函数
#     x=[random.randint(0,1000) for i in range(10**6)]
#     y=heap_sort(x)
#     flag=0
#     for i in range(len(y)-1):
#         if y[i]<y[i+1]:
#             flag=1
#     if flag==1:
#         print("Error")
#     else:
#         print("true")
# test()


    
