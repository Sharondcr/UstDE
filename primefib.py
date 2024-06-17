class prim:
    def __init__(self):
def fib(nums):
    x,y=0,1
    for _ in range(nums):
        x,y = y,x+y
        yield x
for value in fib(10):
    print(value)