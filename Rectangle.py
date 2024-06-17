class Rectangle:
    def __init__(self,length,width):
        self._length=length
        self._width=width
    def calculateArea(self):
        area=self._length*self._width
        print("Area of rectangle",area)
    def calculatePerimeter(self):
        perimeter=2*(self._length+self._width)
        print("Perimeter of rectangle",perimeter)
r=Rectangle(3,4)
r.calculateArea()
r.calculatePerimeter()