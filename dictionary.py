my_stock_list={"TCS":2700,"Infosys":3000,"IDBI":140,"NTPC":220}
"""
print(type(my_stock_list))
my_stock_list["SBI"]= 1700
print(my_stock_list)
print("values",my_stock_list.values())
"""

for stock in my_stock_list:
    print(stock,":",my_stock_list[stock])
my_stock_list.pop("NTPC")
print(my_stock_list)
my_stock_list["IDFC"] = 100