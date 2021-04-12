def main():
    
    s = [1,2,3,4,5,6,7,8,9]
    print(binarySearch(s,12))

def binarySearch(data,target):
    left = 0;
    right = len(data) - 1
    return recurBinarySearch(data,target,left,right)

def recurBinarySearch(data, target,left, right):
    if left > right:
        return (False, -1)
    else:
        mid = (left + right) // 2
        if target == data[mid]:
            return (True, mid)
        elif data[mid] > target:
            return recurBinarySearch(data,target,left,mid-1)
        else:
            return recurBinarySearch(data, target, mid+1, right)

if __name__ == '__main__':
    main()
