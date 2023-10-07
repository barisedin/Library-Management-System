import datetime
import time
from datetime import date, timedelta
class book():


    def __init__(self,bookname,ownername,surname,duedate,price,taken):
        self.bookname=bookname
        self.ownername = ownername
        self.surname = surname
        self.duedate = duedate
        self.price = price
        self.taken = taken


class action():
    global list,mainlist,price,takenlist,d0,today
    price = 50
    #mainlist i sadece kitapların adlarını ve yeni kitapları eklemek için kullanıyorum
    mainlist =["Anna Karenina", "The Great Gatsby", "One Hundred Years of Solitude", "A Passage to India", "Invisible Man",
            "Don Quixote"]
    #götürülen kitaplar buraya yazılacak
    takenlist = []
    list=[]
    #günümüzün tarihini verdim 10 gün sonra kullanıcıdan kitabı geri istemesi için yazdırıyorum
    today=date.today()
    d0 = date (2023,10,3)

    #list listesini objeleri oluşturmak için kullanıcam
    list = mainlist.copy()
    # takenlist = mainlist.copy()

    #the fourth book is taken becasuse of see the programs properties
    takenlist.append(list[3])
    list[0] = book("A Passage to India","barış","edin","2023, 11, 3","150","taken")
    print(list)

    # list[3] = book("A Passage to India","barış","edin","2023, 11, 3","150","taken")
    # takenlist.append(list[3].bookname)


    @staticmethod
    def addbook():
        newbook = input("What is the name of the book: ")
        mainlist.append(newbook.title())
        print(f"{newbook.title()} added the system successfully\n ")

    @staticmethod
    def checkbook():
        num=1
        print(takenlist)
        for x in mainlist:
            if x in takenlist:
                # print(takenlist)
                print(f"{num}. {x} (taken)")
            else:
                print(f"{num}. {x}")
            num += 1


    @staticmethod
    def give_book():
    # this metod gives the book to a user
        nnum=1
        countnum=-1
        for x in mainlist:

            if x not in takenlist:
                # countnum +=1
                print(f"{nnum}. {x}")
                nnum +=1
            if x  in takenlist:
                # print(f"{num}. {x}")
                # nnum += 1
                pass
        num = input("Which book do you want to take (press q for exit): ")

        if num == "q":
            print("\n")
            return
        else:
            num= int(num)
        print(num)
        num=num-1
        # list = mainlist.copy()
        take= (hasattr(list[num],'taken'))


        if take ==True:

            #if book was taken the program gives alert
            print("Sorry this book is taken come back later")

        elif take ==False:
            print(num+countnum)
            print(mainlist)
            print()
            #if book was not taken program gives the book
            name = input("What is your name")
            surname = input("What is your surname")

            returndate = today + +timedelta(days=10)
            list[num+countnum] = book(mainlist[num+countnum],name,surname,returndate,price,True)
            takenlist.append(list[num+countnum].bookname)

            print("This will cost 50 ")
            print(f"You have to return the {mainlist[num+countnum]} on {returndate} ")
            time.sleep(5)

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