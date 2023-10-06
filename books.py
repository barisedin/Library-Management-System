import datetime
import time
from datetime import date, timedelta


class book():

    def __init__(self, bookname, ownername, surname, duedate, price, taken):
        self.bookname = bookname
        self.ownername = ownername
        self.surname = surname
        self.duedate = duedate
        self.price = price
        self.taken = taken


class action():
    global list, mainlist, price, takenlist, d0, today
    price = 50
    mainlist = ["Anna Karenina", "The Great Gatsby", "One Hundred Years of Solitude", "A Passage to India",
                "Invisible Man",
                "Don Quixote"]
    takenlist = []
    today = date.today()
    d0 = date(2023, 10, 3)

    # list = mainlist.copy()

    # the fourth book is taken becasuse of see the programs properties
    takenlist.append("A Passage to India")
    takenlist[0] = book("A Passage to India", "barış", "edin", "2023, 11, 3", "150", "taken")
    # takenlist.append(list[3].bookname)

    @staticmethod
    def addbook():
        newbook = input("What is the name of the book: ")
        mainlist.append(newbook.title())
        print(f"{newbook.title()} added the system successfully\n ")

    @staticmethod
    def checkbook():
        num = 1
        for x in mainlist:
            for i in range(len(takenlist)):
                print(type(i))
                print(takenlist)
                if x in takenlist[i].bookname:
                    print(f"{num}. {x} (taken)")
                else:
                    print(f"{num}. {x}")
                num += 1

    @staticmethod
    def give_book():
        # this metod gives the book to a user
        num = 1
        print(takenlist)
        for x in mainlist:
            for i in range(len(takenlist)):
                # print(x)
                # print(takenlist[i])
                if x == takenlist[i].bookname:
                    print(f"{num} {x} (taken)")

                elif x not in takenlist:
                    print(f"{num}. {x}")
                    num += 1

        num = input("Which book do you want to take (press q for exit): ")

        # name_of_book= mainlist[num-1]

        if num == "q":
            print("\n")
            return
        else:
            num = int(num)
            name_of_book = mainlist[num - 1]



        num = num - 1
        list = mainlist.copy()

        for i in range(len(takenlist)):
            if mainlist[num] == name_of_book:
                take = (hasattr(takenlist[i], 'taken'))

        if take == True:

            # if book was taken the program gives alert
            print("Sorry this book is taken come back later")

        elif take == False:

            # if book was not taken program gives the book
            name = input("What is your name")
            surname = input("What is your surname")

            returndate = today + +timedelta(days=10)
            list[num] = book(mainlist[num], name, surname, returndate, price, True)
            takenlist.append(list[num].bookname)

            print("This will cost 50 ")
            print(f"You have to return the {mainlist[num]} on {returndate} ")
            time.sleep(2)

    @staticmethod
    def return_book():
        print("The taken books list")
        i = 1
        for x in takenlist:
            print(f"{i}.{x}")
            i += 1
        choi = int(input("Which book is going to return"))
        del list[3]
        return_book_name = takenlist[choi - 1]
        list.append(return_book_name)
        takenlist.remove(return_book_name)
        print(takenlist)
        print(list)


print()