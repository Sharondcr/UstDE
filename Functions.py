allowances = {"HRA": 0.4, "DA": 0.30, "TA": 0.15}
deductions = {"PF": 0.12, "Insurance": 5000}

def calculateAllowances(basic):
    total_allowance=0
    for key in allowances:
        total_allowance += allowances[key]*basic
    return total_allowance
print(calculateAllowances(basic))
def calculateDeductions(basic):
    total_deductions=0
    for key in deductions:
        if type(deductions[key]) is not int:
            total_deductions+=deductions[key]*basic
        else:
            total_deductions+=deductions[key]
    return total_deductions
def professionalTax(msal):
    prof_tax=0
    if msal>=8500 and msal<=10000:
        prof_tax = 200
    elif msal > 10000 and msal <=30000:
        prof_tax = 300
    elif msal>30000:
        prof_tax = 500
    return  prof_tax
def calculateSalary():
    print(("-" * 25, "salary calculation : ", "-" * 25))
    basic = int(input("Enter basic salary = "))
    gsal=basic + calculateAllowances(basic)
    ptax=professionalTax(gsal)
    nsal=gsal-ptax-calculateDeductions(basic)
    print("Allowances = ",calculateAllowances(basic))
    print("Deductions = ",calculateDeductions(basic))
    print("Professional Tax = ",ptax)
    print("Gross Salary = ",gsal)
    print("Net salary = ",nsal)