from vector import Vector

def main():
    v = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23
    v[-1] = 45 # inserting element at last index
    print(v[4])
    u = v + v  # we override the __add__ function
    print(u)
    total = 0
    for entry in v:
        total += entry
    print(total)

if __name__ == '__main__':
    main()
