class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.p1 = 0 # front pointer
        self.p2 = 0 # rear pointer
        self.max_len = k

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.max_len # circular
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is not None:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.max_len # circular
            return True
        else:
            return False

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2] is None else self.q[self.p2]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None # front and rear pointer moved

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None # only rear pointer moved

myCircularQueue = MyCircularQueue(3)
myCircularQueue.enQueue(1)
myCircularQueue.enQueue(2)
myCircularQueue.enQueue(3)
myCircularQueue.enQueue(4)
myCircularQueue.Rear()
myCircularQueue.isFull()
myCircularQueue.deQueue()
myCircularQueue.enQueue(4)
myCircularQueue.Rear()