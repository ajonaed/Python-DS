import random


def main():
    print(oddPair([2,2,3,4,6,88,78]))
    print(distinctItem([2, 2, 3, 4, 6, 88, 78]))
    print(listWithSpecificCondition(10))
    # print(englishLetter())
    print(randomShuffle([2, 2, 3, 4, 6, 88, 78]))
    print(eofErrorOnInput())  # Try to fix the function.

def oddPair(data):
    '''
    Write a short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd.
    '''
    count = 0;
    for i in data:
        if i % 2 != 0:
            count += 1
    return True if count>= 2 else False
 

def distinctItem(data):
    '''
    Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other 
    (that is, they are distinct).
    '''
    keeper = set()
    for i in data:
        if i in keeper:
            return False
        else:
            keeper.add(i)
    return True


def listWithSpecificCondition(n):
    '''
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
    '''
    return [i * (i-1) for i in range(1,n+1)]


def englishLetter():
    '''
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [ a , b , c , ..., z ], but without having to type all 26 such
    characters literally.
    '''
    return {i: chr(i) for i in range(97, 123)}


def randomShuffle(data):
    '''
    Python’s random module includes a function shuffle(data) that accepts a
    list of elements and randomly reorders the elements so that each possible
    order occurs with equal probability. The random module includes a
    more basic function randint(a, b) that returns a uniformly random integer
    from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function.
    '''
    # --> return a random number within the range
    for k in range(0, len(data)):
        random_index = random.randint(0, k)
        tmp = data[random_index]
        data[random_index] = data[k]
        data[k] = tmp
    return data

# Try to fix the code.
def eofErrorOnInput():
    # C-1.21
    # Write a Python program that repeatedly reads lines from standard input until an EOFError
    # is raised, and then outputs those lines in reverse order
    #  (a user can indicate end of input by typing ctrl-D).
    done = False
    lines = []
    
    # while not done:
    #     try:
    #             line = input('Enter text, i shall print it in reversed order, ctrl-d to stop')
    #             lines.append(line)
    #     except (EOFError):
    #         for l in lines:
    #             print(l)
    #         done = True

if __name__ == '__main__':
    main()
