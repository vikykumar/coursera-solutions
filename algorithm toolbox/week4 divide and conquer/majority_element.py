# Uses python3
import sys

def get_majority_element(a):
    counts  = dict()
    for i in a:
        counts[i] = counts.get(i,0) + 1
#    print(counts)
        if counts[i] > n/2:
            return 1

    return 0



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(get_majority_element(a))
