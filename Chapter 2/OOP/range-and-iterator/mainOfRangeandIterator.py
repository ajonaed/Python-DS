from range import Range 
from iterator import SequenceIterator

def main():
    # for i in Range(5):
    #     print(i)
    s = SequenceIterator([1,2,3,4,5])
    for i in Range(7):
        # this is giving error as AttributeError: 'SequenceIterator' object has no attribute 'next'
        # print(s.next())
        print(s.__next__()) # Working but this not the appropriate way
 

if __name__ == '__main__':
    main()
