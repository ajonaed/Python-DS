def main():

    s = [1,2,3,4,5,6,7]
    print(binarySearchIterative(s, 9))
    print(reverseListIterative(s))



def reverseListIterative(s):
    start = 0;
    stop = len(s) - 1
    while start <= stop:
        s[start], s[stop] = s[stop], s[start]
        start , stop = start + 1, stop -1
    return s

def binarySearchIterative(s, target):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = (low + high) // 2
        if s[mid] == target:
            return True
        elif s[mid] < target:
            low = mid + 1
        else :
            high = mid - 1
    return False

if __name__ == '__main__':
    main()
