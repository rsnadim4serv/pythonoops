class myStore:
    def __init__(self,storeName:str):
        self.storeName=storeName

    def Vegetables(self):
        print("Working on progess!")

    def DryFruits(self):
        print("DryFruits-Under development!")

    def Carbohydrate(self):
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