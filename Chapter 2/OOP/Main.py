import copy
def main():
    # An Alias
    a = [1,2,3,4]
    print('a list: --> ', a, ', Memory Address: a -->', id(a))
    b = a
    print('b list: --> ', b, ', Memory Address: b -->', id(b))
    b[1] = 5
    print('b list: after b[1] = 5 assignment --> ', b)  # output of b--> [1, 5, 3, 4]
    print('a list: after b[1] = 5 assignment --> ', a)  #output of a--> [1, 5, 3, 4]
    ''' Although we changed the value of b[1], a[1] has also changed. Because b is
    an alias of a. An alias means b is a pointer to the list object which also pointed by a.
    Meaning a and b both pointer pointing to the same memory address.
    '''
    # Shallow Copy
    b = list(a)
    ''' Now, if we created a new instance by above code, this will create a copy of 'a' as a list
    instance. Where both a instance. In short both will be separate copy but yet indirect alias
    of each other.
    '''
    b[1] = 10
    print('Shallow Copy: b --> ', b ,', Memory Address: b -->', id(b)) 
    print('Shallow Copy: a --> ', a, ', Memory Address: a -->', id(a))
    # Note --> Though, above version is shallow copy, out is different from each other. WHY?
    
    #Deep Copy
    ''' We can create deep copy where each of the instance will have own copy by using Python copy
    Module'''
    b = copy.deepcopy(a)
    print('Deep Copy: b --> ', b, ', Memory Address: b -->', id(b))
    print('Deep Copy: a --> ', a, ', Memory Address: a -->', id(a))




if __name__ == '__main__':
    main()
