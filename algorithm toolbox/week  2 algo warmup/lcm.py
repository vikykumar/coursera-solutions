# Uses python3
import sys

def gcd_naive(a, b):
    while True:
        if b == 0:
            break
        t=a % b
        a = b
        b = t

    return a

def lcm_naive(a, b):
    y=gcd_naive(a,b)

    return int(a*b/y)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

