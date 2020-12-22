# python3

class bd :
    def __init__(self,data):
        self.data = data
        self.swaps = []
        self.size = len(data)

    def build_heap(self):

        # The following naive implementation just sorts the given sequence
        # using selection sort algorithm and saves the resulting sequence
        # of swaps. This turns the given array into a heap, but in the worst
        # case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        for i in reversed(range(0, int(self.size/2))):
            self.siftdown(i)

        print(len(self.swaps))
        for i, j in self.swaps:
            print(i, j)


    def siftdown(self, i) :
        max = i
        l = (2*i) + 1
        if l <= self.size - 1 and self.data[l] < self.data[max] :
            max = l
        r = 2*i + 2
        if r <= self.size - 1 and self.data[r] < self.data[max] :
            max = r
        if i != max :
            t= self.data[max]
            self.data[max] = self.data[i]
            self.data[i] = t
            self.swaps.append((i,max))
            self.siftdown(max)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    heap = bd(data)
    heap.build_heap()


if __name__ == "__main__":
    main()
