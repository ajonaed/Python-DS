class Vector:

    def __init__(self, d):
        self._coords = [0] * d 
    
    def __len__(self):
        '''Return True if vector differs from other'''
        return len(self._coords)
    
    def __getitem__(self, j):
        '''Return True if vector differs from other'''
        return self._coords[j]
    
    def __setitem__(self, j, val):
        '''Return True if vector differs from other'''
        self._coords[j] = val
    
    def __add__(self,other):
        '''Return True if vector differs from other'''
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] + other[j]
            return result
    
    def __eq__(self,other):
        '''Return True if vector differs from other'''
        return self._coords == other._coords
    
    def __ne__(self, other):
        '''Return True if vector differs from other'''
        return not self == other
    def __str__(self):
        '''Return True if vector differs from other'''
        return '<'+ str(self._coords)[1:-1]+ '>'
