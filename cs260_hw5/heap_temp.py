import sys


class Heap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def __str__(self):
        return str(self.heapList)

    def makenull(self):
        self.heapList = []

    def insert(self, x):
        self.heapList.append(x)
        self.currentSize = self.currentSize + 1
        if self.currentSize == 2:
            if self.heapList[1] < self.heapList[0]:
                self.swap(0, 1)
        elif self.currentSize >= 3:
            self.upheap(self.currentSize)

    def parent(self, i):
        if i >= self.currentSize:
            return "Index out of bound"
        else:
            result = int((i - 1) / 2)
            if result > self.currentSize - 1:
                return None
            else:
                return result

    def left(self, i):
        if i >= self.currentSize:
            print("Index out of bound")
            return None
        else:
            result = int((i + 1) * 2 - 1)
            if result > self.currentSize:
                return None
            else:
                return result

    def right(self, i):
        if i >= self.currentSize:
            print("Index out of bound")
            return None
        else:
            result = int((i + 1) * 2)
            if result > self.currentSize:
                return None
            else:
                return result

    def swap(self, a, b):
        if a < self.currentSize and b < self.currentSize:
            tmp = self.heapList[a]
            self.heapList[a] = self.heapList[b]
            self.heapList[b] = tmp
        else:
            return "Index out of bound"

    def upheap(self, i):
        while i // 2 > 0:
            if self.heapList[i - 1] < self.heapList[(i // 2) - 1]:
                self.swap(((i // 2) - 1), (i - 1))
            i = i // 2

    def downheap(self, i):
        while (i * 2) + 2 < self.currentSize:
            rc = self.right(i)
            lc = self.left(i)
            if rc is not None or lc is not None:
                if self.heapList[rc] < self.heapList[lc]:
                    mc = rc
                else:
                    mc = lc
            if self.heapList[i] > self.heapList[mc]:
                self.swap(mc, i)
            i = mc

    def inorder(self, i):
        if i < self.currentSize:
            if self.left(i) is not None:
                self.inorder(self.left(i))
            if self.heapList[i] is not None:
                print(str(self.heapList[i]), sep=' ', end=' ', file=sys.stdout, flush=False)
            if self.right(i) is not None:
                self.inorder(self.right(i))

    def preorder(self, i):
        if i < self.currentSize:
            if self.heapList[i] is not None:
                print(str(self.heapList[i]), end=" ")
            if self.left(i) is not None:
                self.preorder(self.left(i))
            if self.right(i) is not None:
                self.preorder(self.right(i))

    def postorder(self, i):
        if i < self.currentSize:
            if self.left(i) is not None:
                self.postorder(self.left(i))
            if self.right(i) is not None:
                self.postorder(self.right(i))
            if self.heapList[i] is not None:
                print(str(self.heapList[i]), end=" ")

    def min(self):
        return self.heapList[0]

    def deletemin(self):
        self.swap(0, self.currentSize - 1)
        self.heapList.remove(self.heapList[self.currentSize - 1])
        self.currentSize = self.currentSize - 1
        self.downheap(0)


if __name__ == "__main__":
    heapTest = Heap()

    # insert test
    print("Insert Test")
    heapTest.insert(5)
    print(heapTest)

    heapTest.insert(7)
    print(heapTest)

    heapTest.insert(4)
    print(heapTest)

    heapTest.insert(2)
    print(heapTest)

    heapTest.insert(1)
    print(heapTest)

    heapTest.insert(3)
    print(heapTest)

    heapTest.insert(8)
    print(heapTest)

    heapTest.insert(10)
    print(heapTest)

    heapTest.insert(9)
    print(heapTest)

    heapTest.insert(6)
    print(heapTest)

    print()

    # parent test
    print("Parent Test")
    print("Index of  the parent of index 3 is:")
    print(heapTest.parent(3))
    print()

    # left test
    print("Left Test")
    print("Index of the left child of index 3 is:")
    print(heapTest.left(3))
    print()

    # right test
    print("Right Test")
    print("Index of the right child of index 1 is:")
    print(heapTest.right(1))
    print()

    # preorder test
    print("Preorder Test")
    heapTest.preorder(0)
    print()

    # preorder test
    print("Inorder Test")
    heapTest.inorder(0)
    print()

    # preorder test
    print("Postorder Test")
    heapTest.postorder(0)
    print()

    # deletemin test
    print("Delete Min Test")
    print(heapTest)
    heapTest.deletemin()
    print(heapTest)
    heapTest.deletemin()
    print(heapTest)
    heapTest.deletemin()
    print(heapTest)
    print()