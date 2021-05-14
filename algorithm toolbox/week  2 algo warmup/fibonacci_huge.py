# Uses python3
import sys

def get_pisano_period(m):
    a = 0
    b = 1
    c = [0,1]
    for i in range(0,m*m):
        c.append((a + b) % m)
        a = b
        b = c[i+2]
        if (a == 0 and b == 1):
            return (i + 1),c

def get_fibonacci_huge_naive(n, m):
    r, d =get_pisano_period(m)
    #print(int(r))
    p= n % r
   # print(d)
    return d[p]

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
