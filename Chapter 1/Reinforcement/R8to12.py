import random
def main():
    
    data = [1, 5, 10, 0, 23]
    negetiveIndices(data)
    rangeParameter(80)
    print()
    print(powerOfTwo(8))
    print(randomChoice(10))

def negetiveIndices(data):
    '''
    Python allows negative integers to be used as indices into a sequence,
    such as a string. If string s has length n, and expression s[k] is used for index
    −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
    the same element?
    In short, if k = -2, python will start the counting -1 from the end of the list.
    Now, I have to find j such that data[j] == data[k]
    '''
    k = -2
    print(data[k], ' --> ', len(data))  # data[k] = 0
    j = k + len(data) # -2 + 5 = 3
    print('j value is: ',j) # j = 3
    print('Data at j: ',data[j]) # data[j] = 0
    print(data[j] == data[k])


def rangeParameter(n):
    '''
    What parameters should be sent to the range constructor, to produce a
    range with values 50, 60, 70, 80?
    '''
    for i in range(50, n+1, 10): # Range Parameter = start: 50, end: 81, increament: 10
        print(i, end=' ')

def powerOfTwo(n):
    '''
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
    '''
    return [2**i for i in range(0,n+1)]


def randomChoice(n):
    '''
    Python’s random module includes a function choice(data) that returns a
    random element from a non-empty sequence. The random module includes
    a more basic function randrange, with parameterization similar to
    the built-in range function, that return a random choice from the given
    range. Using only the randrange function, implement your own version
    of the choice function.
    '''
    # print(random.choice(range(n))) --> return a random number within the range
    return random.randrange(1,n)

if __name__ == '__main__':
    main()
