def insert_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i-1
        temp=a[i]
        while j>=0 and temp<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
import random
a=[random.randint(0,10) for i in range(10)]
print(a)
insert_sort(a)
print(a)
