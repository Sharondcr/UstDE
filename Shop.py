def menu():
    print(" 1.View the Items\n 2.Add item in cart\n 3.Update item in cart\n 4.Remove item from cart\n 5.Exit")
def view(stock):
    for i in stock:
        print(i,':',stock[i])
def vcart(stock,mainstock):
    for i in stock:
        print(i,stock[i],'Rs',stock[i]*mainstock[i])

print('welcome to my store')
stock={'bread':60,'milk':25,'butter':55,'egg':20}
cart={}
menu()
op=int(input("Enter any option = "))
if op not in [1,2,3,4,5]:
    print("Invalid option")
while (op!=6):
    if(op==1):
        view(stock)
        print("Enter next option = ")
    elif(op==2):
        itemname=input("Enter the item to add = ")
        if(itemname not in stock.keys()):
            print("Item not found")
        elif(itemname in cart.keys()):
            print("Item already exists")
        else:
            cart[itemname]=int(input("Enter the quantity = "))
            vcart(cart,stock)
        print("Enter next option = ")
    elif(op==3):
        itemname=input("Enter the item = ")
        if(itemname not in stock.keys()):
            print("Item not found")
        elif(itemname in cart.keys()):
            cart[itemname]=int(input("Enter the Quantity = "))
        else:
            print("Item not found")
            vcart(cart,stock)
    elif(op==4):
        itemname=input("Enter the item to remove = ")
        if(itemname not in stock.keys()):
            print("Item not found")
        else:
            cart.pop(itemname)
        vcart(cart,stock)
        print("Enter next option = ")
    op=int(input(""))
    if op==5:
        total = 0
        itemnum = 0
        for i in cart:
            itemnum += 1
            print(itemnum,".",i,cart[i],cart[i]*stock[i])
            total += cart[i]*stock[i]
            print("total price = ",total)

