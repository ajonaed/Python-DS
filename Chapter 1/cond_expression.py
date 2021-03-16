#Way of writing conditional expression

def foo(param):
    return 5 + param


n = 8

# 1st way of writing Conditional Expression
if n >= 0:
    param = n
else:
    param = -n
print(param)
print(foo(param))
# 2nd way of writing Conditional Expression
param = n if n>0 else -n
print(param)
print(foo(param))
# 3rd way of writing Conditional Expression
print(foo(n if n<= 0 else -n))

