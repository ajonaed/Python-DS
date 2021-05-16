from emptyException import Empty
class ArrayStack:
    ''' LIFO Stack implementation using a Python list as underlying storage

        Operation           Running Time

        S.push(e)               O(1)∗
        S.pop()                 O(1)∗
        S.top()                 O(1)
        S.is empty()            O(1)
        len(S)                  O(1)

        *amortized
    '''

    def __init__(self):
        self._data = []
    
    def __len__(self):
        ''' Return Number of element in the Stack '''
        return len(self._data)
    
    def isEmpty(self):
        ''' Return True if the stack is empty '''
        return len(self._data) == 0
    
    def push(self,e):
        ''' Add element at the end of the Stack '''
        self._data.append(e)
    
    def top(self):
        ''' Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty '''

        if self.isEmpty():
            raise Empty()
        return self._data[-1]
    
    def pop(self):
        ''' Remove and return the element from the top of the stack (i.e., LIFO).
            Raise Empty exception if the stack is empty. 
        '''
        if self.isEmpty():
            raise Empty()
        return self._data.pop()
    
    def __str__(self):
        # return '\n'.join(str(self._data[j]) for j in range(len(self._data)-1, -1, -1))
        temp = ''
        for j in range(len(self._data)-1,-1,-1):
            if j == 0:
                temp += '| ' + str(self._data[j]) + ' |'
            else:
                temp += '| ' + str(self._data[j]) + ' |\n'      
        return temp

        
    


    

