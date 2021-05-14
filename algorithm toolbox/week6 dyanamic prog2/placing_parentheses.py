# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(data):
    n = len(data)
    m = [[0] * (n + 1) for _ in range(n + 1)]
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        m[i][i] = data[i - 1]
        M[i][i] = data[i - 1]
    for s in range(1,n):
        for i in range(1,n-s+1):
            j = i + s
            m[i][j], M[i][j] = min_max(i,j,m,M)
    #write your code here
    return M[1][n]

def min_max(i,j,m,M):
    miin = float("+inf")
    maax = float("-inf")
    for k in range(i,j):
        a = evalt(m[i][k], m[k+1][j], op[k-1])
        b = evalt(m[i][k], M[k+1][j], op[k-1])
        c = evalt(M[i][k], m[k+1][j], op[k-1])
        d = evalt(M[i][k], M[k+1][j], op[k-1])
        miin = min(miin, a, b, c, d)
        maax = max(maax, a, b, c, d)
    return miin, maax

expr = input()
n = len(expr)
digit = [int(expr[i]) for i in range(0, n + 1, 2)]
op = [expr[i] for i in range(1, n, 2)]
print(get_maximum_value(digit))
