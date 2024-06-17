class Primenumber:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        while self.current <= self.end:
            if self.is_prime(self.current):
                prime=self.current
                self.current+=1
                return prime
            else:
                self.current += 1
        raise StopIteration


    def is_prime(self,n):
        if n<2:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True

start=11
end=30
primes=Primenumber(start,end)

for prime in primes:
    print(prime)