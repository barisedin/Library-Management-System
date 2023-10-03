import datetime
import time
from datetime import date
class book():

    def __init__(self,bookname,ownername,surname,duedate,price,taken):
        self.bookname=bookname
        self.ownername = ownername
        self.surname = surname
        self.duedate = duedate
        self.price = price
        self.taken = taken


class action():
    global list,mainlist,price,takenlist
    price = 50
    mainlist =["Anna Karenina", "The Great Gatsby", "One Hundred Years of Solitude", "A Passage to India", "Invisible Man",
            "Don Quixote"]
    takenlist = []
    global d0
    d0 = date (2023,10,3)

    list = mainlist.copy()

    list[3] = book("A Passage to India","barış","edin","2023, 11, 3","150","taken")
    takenlist.append(list[3].bookname)


    @staticmethod
    def addbook():
        newbook = input("What is the name of the book: ")
        mainlist.append(newbook.title())
        print(f"{newbook.title()} added the system successfully\n ")

    @staticmethod
    def checkbook():
        num=1
        for x in mainlist:
            if x in takenlist:
                print(f"{num}. {x} (taken)")
            else:
                print(f"{num}. {x}")
            num += 1
    def give_book(num):
        list = mainlist.copy()
        # a =list[num]
        take= (hasattr(list[num],'taken'))
        if take ==True:
            print("Sorry this book is taken come back later")
        elif take ==False:
            name = input("What is your name")
            surname = input("What is your surname")
            date=input("When do you want to return the book")
            list[num] = book(mainlist[num],name,surname,date,price,True)
            takenlist.append(list[num].bookname)
            print(takenlist)
            # d1 = int(input("When its gonna return (Write as year/ month /day)"))
            # print(type(d0))
            # print(type(d1))

            # days=d0-d1
            # print(f"You have {days.days} to read")
    @staticmethod
    def return_book():
        print("The taken books list")
        i =1
        for x in takenlist:
            print(f"{i}.{x}")
            i +=1
        choi = int(input("Which book is going to return"))
        del list[3]
        return_book_name = takenlist[choi - 1]
        list.append(return_book_name)
        takenlist.remove(return_book_name)
        print(takenlist)
        print(list)





print()