from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class ConsolePrinter(Printer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrinter(Printer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])