# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    i=-1
    j=-1
    for first in range(n):
        if i == -1 or numbers[first] > numbers[i]:
            i = first
    for second in range(n):
        if i != second and (j == -1 or numbers[second] > numbers[j]):
            j = second
    max_product = numbers[i]*numbers[j]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
