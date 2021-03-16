from math import sqrt
def ownSqrt1(x):
    if not isinstance(x,(int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    else:
        return sqrt(x)

print(ownSqrt1(9))

age = -1
while age <= 0:
    try:
        age= int(input('Enter your age in years: '))
        if age <= 0:
            print('Your age must be positive...')
    # If we use raise ValueError, then The execution will be stopped.
    # To keep the execution running, we are using except as try-catch block. 
    except (ValueError):        
        print('Invalid Input!!')
    