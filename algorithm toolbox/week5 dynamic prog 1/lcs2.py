#Uses python3

import sys

def lcs2(a, b):
    m = len(a)
    n = len(b)
    L =  [[float('-inf') ] * (n + 1) for _ in range(m + 1)]
    for i in range(m+1):
        for j in range(n + 1):
            if (i==0 or j== 0):
                L[i][j] = 0
            elif (a[i - 1] == b[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])

    #write your code here
    return L[m][n]

if __name__ == '__main__':
    na = int(input())
    a = input().split()
    nb = int(input())
    b = input().split()


    print(lcs2(a, b))
