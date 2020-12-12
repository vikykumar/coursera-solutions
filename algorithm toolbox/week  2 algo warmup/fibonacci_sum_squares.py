# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    x = []
    x.insert(0, 0)
    x.insert(1, 1)
    sum = 1
    n=n%60
    for i in range(2, n + 2):
        x.insert(i, (x[i - 1] + x[i - 2]) % 10)

    sum = x[n]*x[n+1]
    if n==0:
        return 0
    else:
        return sum%10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
