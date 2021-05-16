from arrayStack import ArrayStack

def main():
    pat = '(()[]{})'
    print(isMatched(pat))


def isMatched(pat):
    lefty = '({['
    righty = ')}]'

    s = ArrayStack()
    for c in pat:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.isEmpty():
                return False
            # print('righty index: ',k)
            # print('lefty index: ', j)
            if righty.index(c) != lefty.index(s.pop()):
                return False
            # if k != j:
            #     return False
    return s.isEmpty()


if __name__ == '__main__':
    main()
