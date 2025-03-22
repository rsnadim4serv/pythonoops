from datetime import date

class Books:
    def __init__(self,bookId:int,bookName:str,author:str,genre:str):
        self.bookId=bookId
        self.bookName=bookName
        self.author=author
        self.genre=genre
        self.bookInfo=[]
    def get_bookInfo(self):
        print(f"{self.bookId}\t\t{self.bookName}\t\t{self.author}\t\t{self.genre}")

class Borrower:
    def __init__(self,borrower:str,email:str,borrowing_date:date,due_date:date,bookID:int):
        self.borrower=borrower
        self.email=email
        self.borrowing_date=borrowing_date
        self.due_date=due_date
        self.bookID=bookID
        self.return_date=""

    def get_borrowerInfo(self):
        print(f"{self.borrower}\t\t{self.email}\t\t{self.borrowing_date}\t\t{self.due_date}\t\t{self.bookID}")
    
    def alertCharge(self,due_date:date):
        if(date.today()>due_date):
            charge=(date.today()-due_date).days * 0.5
        print(f"\nMailto:{self.email}\nDear {self.borrower}, you have to pay {charge}/= for {(date.today()-due_date).days} days")

    def returnTime(self,due_date:date,return_date:date)->int:
        if(return_date>due_date):
            days=(return_date-due_date).days
        return days




class Library_manager:
    def __init__(self,libraryName:str,locAddress:str):
        self.libraryName=libraryName
        self.locAddress=locAddress
        self.books=[]
        self.borrowers=[]

    def add_bookInfo(self,book:Books):
        self.books.append(book)

    def show_bookInfo(self):
        print("-----------------------Our Books Informations----------------------------")
        print("BookID\t\tBookName\t\tAuthorName\t\tGenre")
        for book in self.books:
            book.get_bookInfo()

    def add_borrowerInfo(self,br:Borrower):
        self.borrowers.append(br)

    def show_borrowerInfo(self):
        print("------------------------------Borrowers Informations-----------------------------------")
        print("Borrower\t\tEmail\t\tBorrowingDate\t\tDueDate\t\tBookID")
        for br in self.borrowers:
            br.get_borrowerInfo()
    

if __name__=="__main__":
    library1 =Library_manager("DUET Library","DUET, Gazipur")
    print(f"Welcome to {library1.libraryName}, Our location is at {library1.locAddress}")

    book1 =Books(201,"Python","Jankar Manmud","programming")
    book2 =Books(202,"DSA","Jonathon","technological")

    library1.add_bookInfo(book1)
    library1.add_bookInfo(book2)

    library1.show_bookInfo()

    br1 =Borrower("Nadim","abc@gmail.com",date(2025,1,15),date(2025,2,15),book1.bookId)
    br2 =Borrower("Yusuf","y@gmail.com",date(2025,1,12),date(2025,2,12),book2.bookId)

    library1.add_borrowerInfo(br1)
    library1.add_borrowerInfo(br2)
    library1.show_borrowerInfo()
    #calculate charge with days in no-return type function alertCharge()
    br1.alertCharge(br1.due_date)
    #take days from int return type function returnTime()
    days=br2.returnTime(br2.due_date,date(2025,4,20))
    print(f"\nDear {br2.borrower}, you have to pay {days*0.5}/= for {days} days")
