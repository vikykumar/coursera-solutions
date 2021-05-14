#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    for i in range(0, len(a)-1):
        for j in range(i+1,len(a)):
            if a[j]> a[i]:
                t1 = a[i]
                a[i] = a[j]
                a[j] = t1
            if b[j]> b[i]:
                t2 = b[i]
                b[i] = b[j]
                b[j] = t2
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
