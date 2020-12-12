# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    r = 0
    for i, next in enumerate(text):
        if next in "([{":
            if (i == len(text) - 1) :
                return i+1
            opening_brackets_stack.append(Bracket(next,i))

            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            if len(opening_brackets_stack) == 0 :
                return i +1
            p = opening_brackets_stack.pop()

            if not are_matching(p.char, next) :
                return i+1
            # Process closing bracket, write your code here

            pass
    if len(opening_brackets_stack) != 0 :
        return opening_brackets_stack[-1].position + 1
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
