BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".
        :param id_: Идентификатор (ID) книги
        :param name: Название книги
        :param pages: Число страниц в книге
        """

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name={self.name!r}, pages={self.pages})"


class Library:
    """
    Создание и подготовка к работе объекта "Библиотека".
    :param books: Список книг
    """

    def __init__(self, books: list[Book] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Получить ID для добавления новой книги в библиотеку.
        :return Если запрошенной книги нет, то возвращается 1
        :return: Количество книг в библиотеке
        """

        if len(self.books) == 0:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id):
        """
        Получение индекса книги в списке по её ID.
        :param id_: Идентификатор (ID) книги
        :raise ValueError: Если запрошенной книги нет, то срабатывает ошибка
        :return: Индекс книги
        """

        for index, book in enumerate(self.books):
            if book.id == id:
                return index
        raise ValueError("Нет книги с таким id")


if __name__ == '__main__':
    empty_library = Library() # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
