from arrayStack import ArrayStack

def main():
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    #print(stack)
    print('Top: ',stack.top())
    print('Removed Value: ', stack.pop())
    print(stack)
    print()
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack)
    print('Top: ', stack.top())
if __name__ == '__main__':
    main()
