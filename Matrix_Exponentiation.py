MOD = 1000000007

def matmul(a, b):
    n, k, p = len(a), len(b), len(b[0])
    product = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            s = 0
            for x in range(k):
                s = (s + a[i][x] * b[x][j]) % MOD
            product[i][j] = s
    return product

def identity_matrix(d):
    I = [[0] * d for _ in range(d)]
    for i in range(d):
        I[i][i] = 1
    return I

def expo_power(a, k):
    d = len(a)
    product = identity_matrix(d)
    while k > 0:
        if k % 2 == 1:
            product = matmul(product, a)
        a = matmul(a, a)
        k //= 2
    return product