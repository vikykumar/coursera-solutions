# Uses python3
import sys

def get_change(m):
    #write your code here
    c=0
    c= c+ int((m%10)/5) + int((m%10)%5) + int(m/10)
    return c

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
