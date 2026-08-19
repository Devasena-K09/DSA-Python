from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, title):
        self.title = title
        self.__available = True

    def is_available(self):
        return self.__available

    def borrow(self):

        if self.__available:
            self.__available = False
            print(f"{self.title} borrowed successfully")

        else:
            print(f"{self.title} is not available")

    def return_item(self):
        self.__available = True
        print(f"{self.title} returned successfully")

    @abstractmethod
    def display(self):
        pass


class Book(LibraryItem):

    def __init__(self, title, author):

        super().__init__(title)

        self.author = author

    def display(self):

        print(
            f"Book: {self.title} | Author: {self.author}"
        )


class Library:

    def __init__(self):

        self.items = []

    def add_item(self, item):

        self.items.append(item)

    def show_items(self):

        for item in self.items:
            item.display()


book1 = Book(
    "Python Programming",
    "Guido van Rossum"
)

book2 = Book(
    "Data Structures",
    "Narasimha Karumanchi"
)

library = Library()

library.add_item(book1)
library.add_item(book2)

library.show_items()

book1.borrow()

book1.return_item()
