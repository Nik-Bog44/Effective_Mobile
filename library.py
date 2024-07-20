import json
from typing import List, Dict, Union


class Library:
    def __init__(self, filename: str):
        # Инициализация библиотеки с загрузкой книг из файла
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> List[Dict[str, Union[int, str]]]:
        # Загрузка книг из файла JSON
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                books = json.load(file)
                # Преобразование 'year' к целочисленному типу
                for book in books:
                    book['year'] = int(book['year'])
                return books
        except FileNotFoundError:
            # Если файл не найден, возвращаем пустой список
            return []

    def add_book(self, title: str, author: str, year: int):
        # Проверка, что год является целым числом и положительным
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год должен быть положительным целым числом")

        # Добавление книги в список и сохранение
        self.books.append({
            'id': len(self.books) + 1,  # Простой механизм для уникального ID
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        })
        self.save_books()

    def delete_book(self, book_id: int):
        # Удаление книги по идентификатору
        self.books = [book for book in self.books if book['id'] != book_id]
        self.save_books()

    def search_books(self, search_by: str, search_value: Union[str, int]) -> List[Dict[str, Union[int, str]]]:
        # Поиск книг по заданному критерию
        if search_by not in ["title", "author", "year"]:
            return []  # Возвращаем пустой список, если критерий поиска неверный
        return [book for book in self.books if str(book.get(search_by, '')) == str(search_value)]

    def display_books(self) -> List[Dict[str, Union[int, str]]]:
        # Возвращение списка всех книг в библиотеке
        return self.books

    def update_status(self, book_id: int, new_status: str) -> str:
        # Обновление статуса книги по идентификатору
        for book in self.books:
            if book['id'] == book_id:
                book['status'] = new_status
                self.save_books()
                return f"Статус книги с id {book_id} обновлён на {new_status}"
        return None

    def save_books(self):
        # Сохранение книг в файл
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)