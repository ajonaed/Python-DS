def main():
    a = [1, 2, 3, 6]
    b = [3, 2, 1, 6]
    print(dotProduct(a,b))
    a = listOutOfIndex(a)
    s = 'There are 9 vowels in this string'
    print(countVowels(s))

def dotProduct(a,b):
    '''
    C-1.22 
    Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it returns
    an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.
    '''
    
    if len(a) != len(b):
        return []
    else:
        n = len(a)
        result = [0] * n
        for i in range(n):
            result[i]= a[i] * b[i]
        return result
def listOutOfIndex(a):
    '''
    C-1.23 
    Give an example of a Python code fragment that attempts to write an element
    to a list based on an index that may be out of bounds. If that index
    is out of bounds, the program should catch the exception that results, and
    print the following error message:
    “Don’t try buffer overflow attacks in Python!”
    '''
    try:
        a[7]= ('I was forced to add something')
    except IndexError:
        print('Don\'t try buffer overflow attacks in Python!')

def countVowels(s):
    '''
    C-1.24 
    Write a short Python function that counts the number of vowels in a given
    character string.
    '''
    count = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    return count 
if __name__ == '__main__':
    main()
