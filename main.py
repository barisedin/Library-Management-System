from books import book
from books import action


import time
global list




while True:
    print("Library System")
    print("1. Add book to the system")
    print("2. See books")
    print("3. Take book")
    print("4. Return book")
    print("q. Quit Program")



    choi = input("\nWhat do you want to do:")

    if choi =="1":
        action.addbook()



    if choi == "2":
        print("\n")
        action.checkbook()
        print("\n")
        time.sleep(2)

    elif choi == "3":
        # num = input("Which book do you want to take (press q for exit): ")
        #
        #
        #
        #
        # if num =="q":
        #     print("\n")
        #     continue
        #
        # nnum= int(num)-1
        # action.give_book(nnum)
        print("\n")
        action.give_book()

    elif choi =="4":
        print("\n")
        action.return_book()


    elif choi =="q":
        exit()








