# python3

from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    q = deque()
    for i in range(len(sequence)):
        while q and sequence[i] >= sequence[q[-1]]:
            q.pop()
        q.append(i)
        if i >= m and q and q[0] == i - m:
            q.popleft()
        if i >= m - 1:
            maximums.append(sequence[q[0]])

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

