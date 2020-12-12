# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    x = []
    x.insert(0, 0)
    x.insert(1, 1)
    for i in range(2, n + 1):
        x.insert(i, (x[i - 1] + x[i - 2]) % 10)

    return x[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
