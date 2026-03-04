import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    return np.array([[A[j][i] for j in range(len(A))] for i in range(len(A[0]))])
