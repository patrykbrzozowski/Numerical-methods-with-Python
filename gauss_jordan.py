import numpy as np

def gauss_jordan(A,b):
    n = len(b)
    for k in range(n):
        if np.fabs(A[k][k]) < 1.0e-13:
            for i in range(k+1,n):
                if np.fabs(A[i][k]) > np.fabs(A[k][k]):
                    for j in range(k,n):
                        A[k][j],A[i][j] = A[i][j],A[k][j]
                    b[k],b[i] = b[i],b[k]
                    break
        pivot = A[k][k]
        for j in range(k,n):
            A[k][j] /= pivot
        b[k] /= pivot
        for i in range(n):
            if i == k or A[i][k] == 0:
                continue
            factor = A[i][k]
            for j in range(k,n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    print("Matrix A :" , A)
    print("Result :" , b)
    return b
    

A = [[2, 1, 4],
     [6, 6, 14],
     [4, 14, 19]]

b = [1, 8, 25]


gauss_jordan(A, b)