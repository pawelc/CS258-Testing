# Regression Testing
# ------------------
# The goal of this problem is for you to write a regression tester
# for the Queue class.
# 
# Begin by finding and fixing all of the bugs in the Queue class. Next,
# define the function regression_test to take in a list of enqueue inputs
# and dequeue indicators (the returned list of the previous problem) and
# repeat those method calls using the fixed Queue.
# 
# That is, after fixing the Queue class, create a new Queue instance,
# and call the method corresponding to the indicator in the list
# for each item in the list:
# 
# Call the enqueue function whenever you come across an integer, using that
#     integer as the argument.
# Call the dequeue function whenever you come across the 'dq' indicator.

import array
import random

# Fix this Queue class
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


# An example list of enqueue integers and dequeue indicators
inpts = [(574, 0), ('dq', 0), (991, 0), ('dq', 0), ('dq', 1),
         (731, 0), (97, 0), ('dq', 0), (116, 0), ('dq', 0),
         (464, 0), (723, 0), (51, 0), ('dq', 0), (553, 0),
         (390, 0), ('dq', 0), (165, 0), (952, 0), ('dq', 0),
         ('dq', 0), (586, 0), (894, 0), ('dq', 0), ('dq', 0),
         (125, 0), (802, 0), (963, 0), (370, 0), ('dq', 0),
         ('dq', 0), (467, 0), (274, 0), ('dq', 0), (737, 0),
         (665, 0), (996, 0), (604, 0), (354, 0), ('dq', 0),
         (415, 0), ('dq', 0), ('dq', 0), ('dq', 0), ('dq', 0),
         ('dq', 0), (588, 0), (702, 0), ('dq', 0), ('dq', 0),
         (887, 0), ('dq', 0), (286, 0), (493, 0), (105, 0),
         ('dq', 0), (942, 0), ('dq', 0), (167, 0), (88, 0),
         ('dq', 0), (145, 0), ('dq', 0), (776, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), ('dq', 0), (67, 0), ('dq', 0),
         ('dq', 0), (367, 0), ('dq', 0), (429, 0), (996, 0),
         (508, 0), ('dq', 0), ('dq', 0), (295, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), (997, 0), ('dq', 0), (29, 0),
         (669, 0), ('dq', 0), (911, 0), ('dq', 0), ('dq', 0),
         (690, 0), (169, 0), (730, 0), (172, 0), (161, 0),
         (966, 0), ('dq', 0), (865, 0), ('dq', 0), (348, 0)]


# Write a regression tester for the Queue class
def regression_test(inpts):
    q=Queue(1000)
    for i in range(len(inpts)):
        #print "checking inpt: %s"%(inpts[i][0])
        if inpts[i][0] == "dq":
            res=q.dequeue()
            q.checkRep()
            assert (res and not inpts[i][1]) or (not res and inpts[i][1])
        else:
            res=q.enqueue(inpts[i][0])
            q.checkRep()
            assert (res and not inpts[i][1]) or (not res and inpts[i][1])
    return q
            
from random import randint
def test():
    for _ in range(100):
        size=randint(1,1000)
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
                
    
    

#test()
            
print regression_test(inpts)            
