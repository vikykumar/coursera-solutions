# Uses python3

def calc_fib(n):
    x= []
    x.insert(0,0)
    x.insert(1,1)
    for i in range(2,n+1):
        x.insert(i, x[i-1] + x[i-2])
    return x[n]

n = int(input())
print(calc_fib(n))
