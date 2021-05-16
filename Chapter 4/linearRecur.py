def main():
    s = [4,3,6,2,8]
    print(linearSum(s,len(s)))
    l ='I am from CTG'
    reverseString(s,0,len(s)-1)
    print(s)
    print(power(2,2))
    print(powerInHalfTime(2,4))


def linearSum(s, n):
    if n == 0:
        return 0
    else:
        return linearSum(s,n-1) + s[n-1]


def reverseString(s, start, stop):
    if start < stop:
        s[start], s[stop] = s[stop], s[start]
        reverseString(s,start+1,stop-1)

# O(n) runtime
def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

def powerInHalfTime(x,n):
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        print('---',partial)
        result = partial* partial
        print(result)
        if n%2 == 1:
            result *= x
        return result
if __name__ == '__main__':
    main()
