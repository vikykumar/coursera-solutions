# Uses python3
import sys

def get_change(m):
    coins = (1, 3, 4)
    change = [float ("inf")]*(m+1)
    change[0] = 0
    for i in range(1, m+1):
        for coin in coins:
            if i >= coin:
                numcoin = change[i-coin] + 1
                if numcoin < change[i]:
                    change[i] = numcoin

    #write your code here
    return change[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
