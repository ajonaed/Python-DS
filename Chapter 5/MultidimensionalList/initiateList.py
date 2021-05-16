def main():
    data = [[22,18,709,5,33],[45,32,830,120,750],[4,880,45,66,61]]
    for i in range(len(data)):
        for j in data[i]:
            print(j, end='   ')

        print()
    
    # Right way of creating multidimensional list
    # list = [ [0] * numOfColumns for j in range(numOfRows)], 
    # j is just a counter not related to list value
    twoDlist = [ [0] * 3 for j in range(5)]
    print('[', end='')
    for i in range(len(twoDlist)):
        print('[',end='')
        for j in twoDlist[i]:
            print(j, end='   ')
        print('],', end='')
        print()
    print(']', end='')
if __name__ == '__main__':
    main()
