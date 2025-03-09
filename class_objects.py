class myStore:
    def __init__(self,storeName:str):
        self.storeName=storeName

    def Vegetables(self)->None:
        vdic={"tomato":50,"carrot":40,"cucumber":25,"radish":30}
        print("Here, we have..\nNames\t\tPrice(per kg)\n")
        for k,v in vdic.items():
            print(f"{k}\t\t{v}")
        vname=input("Enter your vegetable: ")
        flag=0
        for prod in vdic.keys():
            if(vname==prod):
                flag=1
                print(f"You have to pay {vdic[prod]}/=")
                pay=int(input("Enter your payment: "))
                if(pay>=vdic[prod]):
                    print(f"You have purchased {prod}, here your change {pay-vdic[prod]}/=")
                else:
                    print("Inadequate balance/money!")
        if(flag==0):
            print("doesn't exit in out products")

    def DryFruits(self)->None:
        print("DryFruits-Under development!")

    def Carbohydrate(self)->None:
        print("Working on Carbohydrate!")

store1 = myStore("MasterStore")
print(f"Welcome to {store1.storeName}")
print("1.Vegetables\n2.DryFruits\n3.Carbohydrates\n4.Exit")
match int(input("Enter your preference: ")):
    case 1:
        store1.Vegetables()
    case 2:
        store1.DryFruits()
    case 3:
        store1.Carbohydrate()
    case _:
        print("Exit, See you later")