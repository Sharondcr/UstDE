prime_number=[1,3,5,11,13,17,19,23]
"""
on_iterator= iter(prime_number)
print(next(on_iterator))
print(next(on_iterator))
"""
class PowThree:
    """class implements an iterator of power of three"""
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 3**self.n
            self.n +=1
            return result
        else:
            raise StopIteration
num=PowThree(3)
i=iter(num)
counter = 1
print("cube of",counter,"=",next(i))
counter+=1
print("cube of",counter,"=",next(i))
counter+=1
print("cube of",counter,"=",next(i))
counter+=1
print("cube of",counter,"=",next(i))
counter+=1
print("cube of",counter,"=",next(i))
counter+=1
print("cube of",counter,"=",next(i))
counter+=1
print(next(i))
