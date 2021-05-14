#Uses python3

import sys

def lcs3(a, b, c):
    p = len(a)
    q = len(b)
    r = len(c)
    L = [[[float('-inf')] * (r + 1) for _ in range(q + 1)] for _ in range(p + 1)]
    for i in range(p + 1):
        for j in range(q + 1):
            for k in range(r + 1):
                if (i==0 or j== 0 or k == 0):
                    L[i][j][k] = 0
                elif (a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]):
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else:
                    L[i][j][k] = max(L[i-1][j][k], L[i][j - 1][k], L[i][j][k - 1], L[i - 1][j - 1][k], L[i - 1][j][k - 1], L[i][j - 1][k - 1])

    #write your code here
    return L[p][q][r]

if __name__ == '__main__':
    na = int(input())
    a = input().split()
    nb = int(input())
    b = input().split()
    nc = int(input())
    c = input().split()

    print(lcs3(a, b, c))
