'''Design a data structure to implement deque data structure'''


class Deque:
    def __init__(self, size):
        self.size=size
        self.list1=[None]*size
        self.count=0
    # Pushes 'X' in the front of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushFront(self, x):
        if self.count<self.size:
            self.list1[self.count]=x
            self.count+=1
            return True
        return False
    # Pushes 'X' in the back of the deque. Returns true if it gets pushed into the deque, and false otherwise.
    def pushRear(self, x):
        if self.count<self.size:
            self.list1=[x]+self.list1[0:self.size-1]
            #print(self.list1)
            self.count+=1
            return True
        return False
    # Pops an element from the front of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popFront(self):
        if self.count==0:
            return -1
        else:
            x=self.list1[self.count-1]
            self.list1[self.count-1]=None
            self.count-=1
            return x

    # Pops an element from the back of the deque. Returns -1 if the deque is empty, otherwise returns the popped element.
    def popRear(self):
        if self.count==0:
            return -1
        else:
            x=self.list1[0]
            self.list1=self.list1[1:]+[None]
            self.count-=1
            return x

    # Returns the first element of the deque. If the deque is empty, it returns -1.
    def getFront(self):
        if self.count==0:
            return -1
        else:
            return self.list1[self.count-1]
    # Returns the last element of the deque. If the deque is empty, it returns -1.
    def getRear(self):
        if self.count==0:
            return -1
        else:
            return self.list1[0]

    # Returns true if the deque is empty. Otherwise returns false.
    def isEmpty(self):
        if self.count==0:
            return True
        return False

    # Returns true if the deque is full. Otherwise returns false.
    def isFull(self):
        if self.count==self.size:
            return True
        return False
