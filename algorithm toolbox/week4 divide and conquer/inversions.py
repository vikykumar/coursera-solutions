# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a, b, left, ave, right)
    #write your code here
    return number_of_inversions

def merge(a, b, left, ave, right):
    inv = 0
    i = left
    j = ave
    k = left
    while i < ave and j < right:
        if a[i] > a[j]:
            inv += ave - i
            b[k] = a[j]
            k += 1
            j += 1
        else:
            b[k] = a[i]
            k += 1
            i += 1
    while i < ave:
        b[k] = a[i]
        k += 1
        i += 1
    while j < right:
        b[k] = a[j]
        k += 1
        j += 1
    for i in range(left,right):
        a[i] = b[i]

    return inv

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
