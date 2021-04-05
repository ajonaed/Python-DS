# R 1.1 --> A write a function which takes two integer values and returns
# True if n is multiple of m, that is n = mi for some integer i and False otherwise

def main():
    print(isMultiple(101,5))
    print(isEven(100))
    data = [1,5,10,0,23]
    print(minMax(data))
    print(squaresOfNum(5))
    print(squaresOfNumLC(5))
    print('SUM of square of odd till n: ',squaresOfODDNum(10))
    print('SUM of square of odd LC till n: ', squaresOfODDNumLC(10))
def isMultiple(n, m):
    '''
    Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    '''
    return True if n % m == 0 else False


def isEven(n):
    '''
    Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
    '''
    # any even power of -1 will be 1, odd power of -1 will be -1
    return True if (-1)**n == 1 else False
def minMax(data):
    '''
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
    '''
    if len(data) == 1:
        return (data[0], data[0])
    else:
        min = float('inf')
        max = float('-inf')
        for i in data:
            if min > i:
                min = i
            if max < i:
                max = i
        return (min,max)


def squaresOfNum(n):
    '''
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n. 
    '''
    try:
        nSum = 0
        for i in range(n):
            nSum += i**2
        return nSum
    except Exception as excpt:
        print('Error! ', excpt)
    return

def squaresOfNumLC(n):
    '''
    Give a single command that computes the sum from Exercise R-1.4, relying
    on Python’s comprehension syntax and the built-in sum function. 
    '''
    return sum([i**2 for i in range(n)])


def squaresOfODDNum(n):
    '''
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n. 
    '''
    try:
        nSum = 0
        for i in range(n):
            if i % 2 == 1:
                nSum += i**2
        return nSum
    except Exception as excpt:
        print('Error! ', excpt)
    return

def squaresOfODDNumLC(n):
    '''
    Give a single command that computes the sum from Exercise R-1.6, relying
    on Python’s comprehension syntax and the built-in sum function.
    '''
    return sum([i**2 for i in range(n) if i % 2 == 1])

if __name__ == '__main__':
    main()
