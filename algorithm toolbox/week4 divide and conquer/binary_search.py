# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    while left!=right:
        m = (left + right)/2
        m = int(m)
        if a[m] == x:
            return m
        elif a[m] > x:
            right = m
        elif a[m] < x:
            left = m+1
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    a = data[1 : ]
    data = list(map(int, input().split()))
    for x in data[1:]:
        binary_search(a,x)
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
