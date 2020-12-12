# Uses python3
import sys

def fibonacci_sum_naive(n):
    x = []
    x.insert(0, 0)
    x.insert(1, 1)
    r = 60
    sum = 1
    if n == 0:
        return 0
    elif n < r:
        for i in range(2, n + 1):
            x.insert(i, (x[i - 1] + x[i - 2]) % 10)
            sum = sum + x[i]
    else:
        p = n % 60
        if p== 0:
            sum = 0
        else:
            for c in range(2, p + 1):
                x.insert(c, (x[c - 1] + x[c - 2]) % 10)
                sum = sum + x[c]

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))