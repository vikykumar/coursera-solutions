# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = l
    i = l
    while i <= r:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
            i += 1
        elif a[i] > x:
            a[i], a[r] = a[r], a[i]
            r -= 1
        else:
            i += 1

    return [j, r]


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0] - 1);
    randomized_quick_sort(a, m[1] + 1, r);


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
