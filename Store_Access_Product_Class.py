class Product:
    def __init__(self, prodName:str,price:float,quantity:int):
        self.prodName=prodName
        self.price=price
        self.quantity=quantity

    def get_prodInfo(self):
        print(f"{self.prodName}\t${self.price}\t{self.quantity}pcs")
    
    def get_Price(self)->float:
        return self.price
    
    def prodPurchase(self,purQuantity:int):
        self.quantity=self.quantity-purQuantity

class Store:
    def __init__(self,storeName:str):
        self.storeName=storeName
        self.prods=[]

    def addProducts(self,prod:Product):
        self.prods.append(prod)

    def showProducts(self):
        print("Products Price Quantity")
        print("------------------------")
        for prod in self.prods:
            prod.get_prodInfo()
            #print(f"{prod.prodName} ${prod.price} {prod.quantity}pcs")

    def sellProduct(self,choosenProd:str,purQuantity:int):
        flag=0
        for prod in self.prods:
            if(prod.prodName.lower()==choosenProd.lower()):
                flag=1
                if(prod.quantity==0):
                    print(f"Sorry! Stock Out ")
                    break
                elif(purQuantity>prod.quantity):
                    print(f"No enough stock for {prod.prodName}\nTry to purchase less than equal to {prod.quantity}")
                    break
                else:
                    prod.prodPurchase(purQuantity)
                    print(f"You have to pay ${purQuantity*prod.get_Price()}")
                    pay=float(input("Enter your payment: "))
                    if(pay>=prod.get_Price()):
                        print(f"You have purchased {prod.prodName}, your change ${pay-purQuantity*prod.get_Price()}")
                    else:
                        print("Insufficient Balance!")
        if(flag==0):
            print("Choosen Product Not Found!")

if __name__== "__main__":
    store1 =Store("LeverageTech")
    print(f"Welcome to {store1.storeName}, Here you have\n")
    #object of Product class
    Laptop = Product("Laptop",42.5,15)
    #object of Store class use object of Product class to add products
    store1.addProducts(Laptop)
    realme = Product("Realme",26.25,12)
    store1.addProducts(realme)
    sumsung = Product("Sumsung",35.45,21)
    store1.addProducts(sumsung)
    ps5 = Product("PS5",74.63,8)
    store1.addProducts(ps5)
    #Show all products
    store1.showProducts()
    while True:
        chProd=input("Enter your product name: ")
        purQn=int(input("How many? - "))
        store1.sellProduct(chProd,purQn)
        print("\n")
        store1.showProducts()
        exit=input("Enter Yes to Exit or otherwise Enter anything to Continue: ")
        if(exit.lower()=="yes"):
            break


