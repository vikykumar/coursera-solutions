# Uses python3
import sys
import itertools

def partition3(W, n, items):
    c = 0
    T = [[0] * (n + 1) for _ in range(W + 1)]
    for i in range(1, W + 1):
        for j in range(1, n + 1):
            T[i][j] = T[i][j - 1]
            if items[j - 1] <= i:
                T[i][j] = max(T[i - items[j - 1]][j - 1] + items[j - 1], T[i][j - 1])
            if T[i][j] == W: c += 1

    if c < 3:
        print('0')
    else:
        print('1')

if __name__ == '__main__':
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n < 3:
        print('0')
    elif total_weight % 3 != 0:
        print('0')
    else:
        partition3(total_weight // 3, n, item_weights)


