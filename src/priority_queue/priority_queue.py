class PriorityQueue:
    def __init__(self, arr=[]) -> None:
        self.arr = arr
        self.hs = len(arr)
        self.__build_heap()

    def __heapify(self, i: int):
        """Assume sub-nodes of i are all valid heaps.
        Compare i with left & right children, swap and continue downwards.
        """
        idx = i
        l, r = idx * 2 + 1, idx * 2 + 2
        if l < self.hs and self.arr[idx] < self.arr[l]:
            idx = l
        if r < self.hs and self.arr[idx] < self.arr[r]:
            idx = r
        if idx != i:
            self.arr[i], self.arr[idx] = self.arr[idx], self.arr[i]
            self.__heapify(idx)

    def __build_heap(self):
        """Obvisously, for 0-indexed arr tree, [n/2...n) are leaf nodes.
        Iterate non-leaf nodes from bottom to top and heapify.
        """
        for i in range(self.hs // 2 - 1, -1, -1):
            self.__heapify(i)

    def __increase_key(self, i, e):
        pass

    def heap_sort(self):
        """Heap sort self.arr; note that heap size will become zero."""
        while self.hs:
            self.arr[0], self.arr[self.hs - 1] = self.arr[self.hs - 1], self.arr[0]
            self.hs -= 1
            self.__heapify(0)

    def top(self):
        return self.arr[0]

    def pop(self):
        pass

    def push(self, e):
        pass


if __name__ == "__main__":
    q = PriorityQueue([1, 2, 3, 4])
    print("Begin:", q.arr)
    print("Top:", q.top())
