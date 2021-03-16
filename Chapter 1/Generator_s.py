# Without Genertors
# def factors(n):
#     results = []
#     for k in range(1,n+1):
#         if n % k == 0:
#             results.append(k)
#     return results

# print(factors(100))

# With Generators

def factors1(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k

# Generator by using yield doesn't generate whole sequence at whole. 
# we have to request for the next value. Below everytime we call next it started from
# beginning. 

i = 0;
while i< 3:
    print('1st: ', next(factors1(100)))
    i += 1
