def main():
    s = [1, 2, 3, 4, 5]
    print(prefix_average_quadratic(s))
    # print(prefix_average_linear(s))

def prefix_average_quadratic(data):
    n = len(data)
    A = [0] * n
    for j in range(n):
        
        total = 0
        for i in range(j+1):
            total += data[i]
        A[j] = total / (j+1)
    return A

def prefix_average_linear(data):
    n = len(data)
    A = [0] * n
    total = 0
    for j in range(n):
        total += data[j]
        A[j] = total /(j+1)
    return A

if __name__ == '__main__':
    main()
