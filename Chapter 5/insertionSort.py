def main():
    a = [ 9,1,3,2,7,8,0]
    print(insertionSort(a))


def insertionSort(a):
    for i in range(1, len(a)):
        cur = a[i]
        j = i

        while j > 0 and a[j-1] > cur:
            a[j] = a[j-1]
            j -= 1
        a[j] = cur
    return a


if __name__ == '__main__':
    main()
