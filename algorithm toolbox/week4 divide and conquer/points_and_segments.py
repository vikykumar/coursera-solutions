# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    #write your code here
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':

    s, p = [int(i) for i in input().split()]
    comb = list()
    for i in range(s):
        a, b = [int(i) for i in input().split()]
        comb.append((a, 'l'))
        comb.append((b, 'r'))

    points = input().split()
    for i in points:
        comb.append((int(i), 'p'))

    comb.sort()

    count = 0
    lottery = dict()
    for c in comb:
        if c[1] == 'l':
            count += 1
        elif c[1] == 'r':
            count -= 1
        else:
            lottery[c[0]] = count

    for point in points:
        print(lottery[int(point)], end = ' ')
