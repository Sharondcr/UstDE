#generator is a function that returns an iterator that produces a sequence of values
#when iterated over

"""
def custom_generator(n):
    value = 0
    while value <n:
        yield  value
        value +=1
for value in custom_generator(10):
    print(value)

"""

"""
cubes_generator=(i*i*i for i in range(5))
for i in cubes_generator:
    print(i)
"""
"""
class PowerThree:
    def __init__(self,max=0):
        self.n=0;
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 3**self.n
        self.n+=1
        return result
def GenPowerThreee(max=0):
    value=0
    while value < max:
        yield  3**value
        value +=1

"""
def fib(nums):
    x,y=0,1
    for _ in range(nums):
        x,y = y,x+y
        yield x
def square(nums):
    for nums in nums:
        yield  nums**2
for value in fib(10):
    print(value)
for value in square((fib(4))):
    print(value)





