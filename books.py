import datetime
import time
from datetime import date, timedelta


class book():

    def __init__(self, bookname, ownername, surname, duedate, price):
        self.bookname = bookname
        self.ownername = ownername
        self.surname = surname
        self.duedate = duedate
        self.price = price



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
    takenlist[0] = book("A Passage to India", "barış", "edin", "2023, 11, 3", "150")


    @staticmethod
    def addbook():
        newbook = input("What is the name of the book: ")
        mainlist.append(newbook.title())
        print(f"{newbook.title()} added the system successfully\n ")

    @staticmethod
    def checkbook():
        place=1
        for x in mainlist:
            take =False
            for i in range(len(takenlist)):
                if x == takenlist[i].bookname:
                    take=True

                else:
                    if take==True:
                        pass
                    else:
                        take=False
                        continue

            if take == True:
                # print(take)
                print(f"{place}. {x} (taken)")
            else:
                # print(take)
                print(f"{place}. {x}")
            place +=1
        pass
    @staticmethod
    def give_book():
        place = 1
        list =[]
        print(list)
        for x in mainlist:
            take =False
            for i in range(len(takenlist)):
                if x == takenlist[i].bookname:
                    take=True

                else:
                    if take==True:
                        pass

            if take == False:

                list.append(x)
                print(f"{place}. {x}")
                place +=1

        num = input("Which book do you want to take (press q for exit): ")

        if num == "q":
            print("\n")
            return
        else:
            num = int(num)
            num = num - 1
            name_of_book = list[num]

        name = input("What is your name")
        surname = input("What is your surname")
        last_element=len(takenlist)
        returndate = today + +timedelta(days=10)
        takenlist.append(name_of_book)
        takenlist[last_element] = book(list[num], name, surname, returndate, price)
        print("This will cost 50 ")
        print(f"You have to return the {mainlist[num]} on {returndate} ")
        time.sleep(2)

    @staticmethod
    def return_book():
        print("The taken books list")
        i = 1
        for x in takenlist:
            print(f"{i}.{x.bookname}")
            i += 1
        choi = int(input("Which book is going to return: "))
        # del list[3]
        return_book_name = takenlist[choi - 1]

        takenlist.remove(return_book_name)