#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__stack1 = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.__stack1) == 0:
            self.__stack1.append(a)
        elif a >= self.__stack1[-1]:
            self.__stack1.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if len(self.__stack1) != 0 and self.__stack[-1] == self.__stack1[-1]:
            self.__stack1.pop()
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__stack1[-1]


if __name__ == '__main__':
    stack = StackWithMax()
#    stack1 = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
 #           if len(stack1) == 0:
  #              stack1.Push(int(query[1]))
   #         elif int(query[1]) > stack1[-1]:
    #            stack1.Push(int(query[1]))
     #       else :
      #          pass
        elif query[0] == "pop":
            stack.Pop()
       #     if int(stack[1]) == stack1[-1]:
        #        stack1.Pop()
         #       stack.Pop()
          #  else :
           #     stack.pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
