'''
Time complexity:O(1)
and space Comlexity:O(1)
'''
class book:
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price

    def purchase(self, noc):
        self.__noc = noc
        self.total = self.price * self.__noc

        if self.__noc <= 100:
            self.discount = 0
        elif self.__noc <= 200:
            self.discount = self.total * 0.10
        elif self.__noc <= 300:
            self.discount = self.total * 0.20
        elif self.__noc <= 400:
            self.discount = self.total * 0.30
        else:
            self.discount = self.total * 0.50
        self.grandtotal = self.total - self.discount

    def bookdetalis(self):
        print("BOOK DETAILS")
        print("Name :", self.title)
        print("Author :", self.author)
        print("Price :", self.price)
        print("No. of Copies :", self.__noc)
        print("Discount :", self.discount)
        print("Grand Total :", self.grandtotal)

    def bookpurchase(self):
        noc = int(input("Enter number of copies: "))
        self.purchase(noc)
        self.bookdetalis()

title = input("Enter book title: ")
author = input("Enter author name: ")
publisher = input("Enter publisher name: ")
price = float(input("Enter book price: "))
b = book(title, author, publisher, price)
b.bookpurchase()
