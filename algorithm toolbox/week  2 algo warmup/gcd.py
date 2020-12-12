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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
