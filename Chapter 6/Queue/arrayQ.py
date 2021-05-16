from emptyException import Empty

class ArrayQueue:
    '''FIFO queue implementation using a Python list as underlying storage.'''

    DEFAULT_CAPACITY = 10

    def __init__(self):
        '''Create an empty queue.'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        '''Return the number of elements in the queue.'''
        return self._size
    
    def isEmpty(self):
        '''Return True if the queue is empty.'''

        return self._size == 0
    
    def forntElement(self):
        '''
        Return(but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        '''
        if self.isEmpty():
            raise Empty('Queue is Empty!')
        return self._data[self._front]
    
    def dequeue(self):
        '''Remove and return the first element of the queue(i.e., FIFO).
        Raise Empty exception if the queue is empty.'''

        if self.isEmpty():
            raise Empty('Queue is Empty!')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        '''By  doing following code, we maintain THETA(n) memory space, when we have size 
        1/4th of the length of the Q
        '''
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data // 2))
        return answer
    
    def enqueue(self,data):
        
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        cur = (self._front + self._size) % len(self._data)
        self._data[cur] = data
        self._size += 1
    
    def _resize(self, cap):
        
        oldData = self._data
        walk = self._front
        self._data = [None] * cap
        for k in range(self._size):
            self._data[k] = oldData[walk]
            walk = (1 + walk) % len(oldData)
        self._front = 0
    
    def __str__(self):
        cur = self._front
        for i in range(self._size):
            print(i,'th Position : ',self._data[cur])
            cur = (cur + 1) % len(self._data)
        return ' End Of the Queue '


