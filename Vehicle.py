class Vehicle:
    def __init__(self,max_speed,mileage):
        self._max_speed=max_speed
        self._mileage=mileage
    def seatingCapacity(self,capacity=50):
        print(f'seat capacity is {capacity}')
    def totalFare(self,capacity):
        return capacity*100
class Bus(Vehicle):
    def totalFare(self,capacity=50):
        total_amount=super().totalFare(capacity)
        main_charge=total_amount*0.1
        final_charge=total_amount+main_charge
        return final_charge
b=Bus(200,50)
b.seatingCapacity()
print(b.totalFare())


