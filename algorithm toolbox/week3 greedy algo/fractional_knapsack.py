# Uses python3
import sys

def get_optimal_value(capacity, val_by_wt , dic):
    value = 0.0
    for i in range(n):
        if capacity == 0:
            return value
        temp = min(capacity, dic[val_by_wt[i]])
        value = value + val_by_wt[i]*temp
        capacity = capacity - temp
    # write your code here
    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    val_by_wt = []
    dic = {}
    for i in range(n):
        values, weights = map(int, input().split())
        val_by_wt.append(values / weights)
        dic[val_by_wt[i]] = weights
    val_by_wt.sort(reverse=True)
    opt_value = get_optimal_value(capacity, val_by_wt, dic)
    print("{:.4f}".format(opt_value))
