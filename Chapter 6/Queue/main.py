from arrayQ import ArrayQueue


def main():
    q = ArrayQueue()
    q.enqueue(9)
    q.enqueue(8)
    q.enqueue(7)
    q.enqueue(6)
    q.enqueue(5)
    q.enqueue(4)
    print(q)
    q.dequeue()
    print(q)




if __name__ == '__main__':
    main()
