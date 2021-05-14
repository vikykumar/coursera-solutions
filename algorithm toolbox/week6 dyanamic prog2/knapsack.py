# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    T = [[0] * (W + 1) for _ in range(len(w) + 1)]
    for i in range(1,len(w)+1):
        for j in range(1,W+1):
            T[i][j] = T[i-1][j]
            if w[i-1] <= j:
                T[i][j] = max((T[i-1][j-w[i-1]] + w[i-1]), T[i-1][j])

    return T[len(w)][W]

if __name__ == '__main__':
    W, n = map(int, input().split())
    w = list(map(int, input().split()))
    print(optimal_weight(W, w))
