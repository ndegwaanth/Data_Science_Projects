import numpy as np


def test_matid(m, n, p, q, rs):
    np.random.seed(rs)
    A = np.random.random((m, n))
    B = np.random.random((n, p))
    C = np.random.random((p, q))

    # Identity matrices
    I1 = np.eye(m)  # Identity matrix of size m (pre-multiply)
    I2 = np.eye(q)  # Identity matrix of size q (post-multiply)

    # Left-hand side calculation
    LHS = np.dot(I1, np.dot(C, np.dot(B, A))).T
    LHS = np.dot(LHS, I2)

    # Right-hand side calculation
    RHS = np.dot(C.T, np.dot(B.T, np.dot(A.T, I2)))

    return LHS, RHS


# Example test case
m = 4
n = 4
p = 2
q = 3
a1, a2 = test_matid(m, n, p, q, 75)
print(a1)
print(a2)