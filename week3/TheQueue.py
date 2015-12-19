import array
from random import randint

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)

# Add test code to test() that achieves 100% coverage of the 
# Queue class.
def test():
    for _ in range(100):
        size=randint(0,1000)
        q=Queue(size)
        q.checkRep()
        
        testQueue=[]
        for i in range(size + randint(1,10)):
            el = randint(1,1000)
            ret = q.enqueue(el)
            q.checkRep()
            if i < size:
                assert ret
                testQueue.append(el) 
            else:
                assert not q.empty()
                assert q.full()
                assert not ret
                
        for i in range(size + randint(1,10)):
            ret = q.dequeue()
            q.checkRep()
            if i < size:
                assert ret
                assert ret == testQueue.pop(0)
            else:
                assert q.empty()
                assert not q.full()
                assert not ret
                
    
    

test()