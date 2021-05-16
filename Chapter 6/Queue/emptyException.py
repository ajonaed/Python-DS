
class Empty(Exception):

    def __init__(self):
        self._message = 'Stack is Empty'
        super().__init__(self._message)
