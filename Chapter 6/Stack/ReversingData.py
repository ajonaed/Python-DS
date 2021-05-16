import os.path
from arrayStack import ArrayStack
def main():
    filePath = 'Chapter 6/test.txt'
    print('File Exist: ',os.path.exists(filePath))
    S = ArrayStack()
    ''' Reading the file line by line and '''
    with open(filePath) as file:
        for line in file:
            '''Right Strip new line has minimal affect. but If we are required to print the
            file we should strip new line from right, then add that when creating the same file '''
            S.push(line.rstrip('\n'))
           # S.push(line)
    print(S)
    output = open('Chapter 6/test.txt','w')
    while not S.isEmpty():
        line = S.pop() + '\n'
        #print(line)
        #line = S.pop()
        output.write(line)
    output.close()
    



if __name__ == '__main__':
    main()

