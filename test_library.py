import unittest
from library import Library

import os


class TestLibrary(unittest.TestCase):
    """
    Класс для тестирования методов класса Library.
    Наследует unittest.TestCase, что позволяет использовать функционал библиотеки unittest.
    """

    def setUp(self):
        """
        Метод для подготовки окружения перед каждым тестом.
        Создает новый экземпляр Library и использует временный файл для тестов.
        """
        self.filename = 'test_data.json'  # Имя временного файла для хранения данных
        self.library = Library(self.filename)  # Создаем экземпляр Library

    def tearDown(self):
        """
        Метод для очистки после выполнения тестов.
        Удаляет временный файл, если он существует.
        """
        if os.path.exists(self.filename):  # Проверяем, существует ли файл
            os.remove(self.filename)  # Удаляем файл

    def test_add_book(self):
        """
        Тестирование метода add_book.
        Проверяет, что книга добавляется корректно.
        """
        self.library.add_book("Test Book", "Test Author", 2024)  # Добавляем книгу
        books = self.library.display_books()  # Получаем список всех книг
        self.assertEqual(len(books), 1)  # Проверяем, что в списке одна книга
        self.assertEqual(books[0]['title'], "Test Book")  # Проверяем, что название книги совпадает

    def test_add_book_invalid_year(self):
        """
        Тестирование метода add_book с некорректным годом.
        Проверяет, что возникает ошибка при попытке добавить книгу с нечисловым годом.
        """
        with self.assertRaises(ValueError):  # Ожидаем исключение ValueError
            self.library.add_book("Invalid Year Book", "Test Author",
                                  "abc")  # Пытаемся добавить книгу с некорректным годом

    def test_delete_book(self):
        """
        Тестирование метода delete_book.
        Проверяет, что книга удаляется по id.
        """
        self.library.add_book("Book to Delete", "Test Author", 2024)  # Добавляем книгу
        book_id = self.library.display_books()[0]['id']  # Получаем id добавленной книги
        self.library.delete_book(book_id)  # Удаляем книгу по id
        books = self.library.display_books()  # Получаем список всех книг
        self.assertEqual(len(books), 0)  # Проверяем, что список книг пуст

    def test_delete_nonexistent_book(self):
        """
        Тестирование удаления несуществующей книги.
        Проверяет, что список книг не изменяется при попытке удалить несуществующую книгу.
        """
        self.library.delete_book(999)  # Пытаемся удалить книгу с несуществующим id
        books = self.library.display_books()  # Получаем список всех книг
        self.assertEqual(len(books), 0)  # Проверяем, что список книг не изменился

    def test_search_books_by_title(self):
        """
        Тестирование метода search_books по title.
        Проверяет, что поиск книги по title возвращает правильную книгу.
        """
        self.library.add_book("Search Book", "Test Author", 2024)  # Добавляем книгу
        books = self.library.search_books("title", "Search Book")  # Ищем книгу по title
        self.assertEqual(len(books), 1)  # Проверяем, что найдена одна книга
        self.assertEqual(books[0]['title'], "Search Book")  # Проверяем, что название книги совпадает

    def test_search_books_by_year(self):
        """
        Тестирование метода search_books по году.
        Проверяет, что поиск книги по году возвращает правильные книги.
        """
        self.library.add_book("Year Search Book", "Test Author", 2024)  # Добавляем книгу
        books = self.library.search_books("year", 2024)  # Ищем книги по году
        self.assertEqual(len(books), 1)  # Проверяем, что найдена одна книга
        self.assertEqual(books[0]['title'], "Year Search Book")  # Проверяем, что название книги совпадает

    def test_display_books(self):
        """
        Тестирование метода display_books.
        Проверяет, что отображение всех книг возвращает корректный список книг.
        """
        self.library.add_book("Display Book", "Test Author", 2024)  # Добавляем книгу
        books = self.library.display_books()  # Получаем список всех книг
        self.assertEqual(len(books), 1)  # Проверяем, что в списке одна книга
        self.assertEqual(books[0]['title'], "Display Book")  # Проверяем, что название книги совпадает

    def test_update_status(self):
        """
        Тестирование метода update_status.
        Проверяет, что статус книги обновляется корректно.
        """
        self.library.add_book("Status Book", "Test Author", 2024)  # Добавляем книгу
        book_id = self.library.display_books()[0]['id']  # Получаем id добавленной книги
        self.library.update_status(book_id, "выдана")  # Обновляем статус книги
        books = self.library.display_books()  # Получаем список всех книг
        self.assertEqual(books[0]['status'], "выдана")  # Проверяем, что статус книги обновлен

    def test_update_status_nonexistent_book(self):
        """
        Тестирование обновления статуса несуществующей книги.
        Проверяет, что при попытке обновить статус несуществующей книги ничего не происходит.
        """
        result = self.library.update_status(999, "в наличии")  # Пытаемся обновить статус книги с несуществующим id
        self.assertIsNone(result)  # Проверяем, что результат выполнения метода None


if __name__ == "__main__":
    unittest.main()  # Запуск всех тестов, если этот файл выполняется как основной
