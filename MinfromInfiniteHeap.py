class SmallestInfiniteSet:

    def __init__(self):
        self.infset = set()
        self.numinfset = 1

    def popSmallest(self) -> int:
        if self.infset:
            temp = min(self.infset)
            self.infset.remove(temp)
            return temp
        self.numinfset += 1
        return self.numinfset-1

    def addBack(self, num: int) -> None:
        if num < self.numinfset:
            self.infset.add(num)

