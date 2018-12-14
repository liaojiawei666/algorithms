import numpy as np
def MATRIX_CHAIN_ORDER(p):
    n=len(p)-1
    m=np.zeros([n,n])
    s=np.zeros([n,n])
    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            m[i,j]=np.inf
            for k in range(i,j):
                q=m[i,k]+m[k+1,j]+p[i]*p[k+1]*p[j+1]
                if q<m[i,j]:
                    m[i,j]=q
                    s[i,j]=k
    return m,s

# import random
# x=[10,100,5,50]
# m,s=MATRIX_CHAIN_ORDER(x)
# print(x)
# print(m[0,2])