class Author:
    all = []
    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance (value, str):
            self._name= value

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def  total_royalties(self):
        totals = [contract.royalties for contract in self.contracts()]
        summ = 0
        for i in totals:
            summ += i
        return summ


class Book:
    all = []
    def __init__(self, title):
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if isinstance (value, str):
            self._title= value

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Expected an Author instance")
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]