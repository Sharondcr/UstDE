import datetime

today = datetime.date.today()
year=today.year

class Company:
    def __init__(self,cname):
        self._cname= cname
    def displayCname(self):
        print("Company Name = ",self._cname)
    def address(self):
        return "Technopark"+" "+"Trivandrum"
class Employee:
    def __init__(self,fname,lname,yob):
        self._fname=fname
        self._lname=lname
        self._age=yob
    def address(self):
        print("Company Address ",super().address())
        self.address()
    def getEmpDetails(self):
        print("Full Name :",self._fname,"",self._lname)
        print("Age: ",self._age)
e=Employee("Sharon","Dcruz",1980)
e.getEmpDetails()
e=Employee("manas","joshi",2007)
e.getEmpDetails()