from library import Library  # Импортируем класс Library из модуля library


def main():
    library = Library('data.json')  # Создаем экземпляр класса Library и загружаем данные из файла data.json

    while True:
        # Выводим меню пользователя
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отображать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")  # Получаем выбор пользователя

        if choice == '1':
            # Добавление книги
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            try:
                year = int(year)  # Преобразуем год в целое число
                library.add_book(title, author, year)
                print(f"Книга '{title}' добавлена в библиотеку")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            # Удаление книги
            book_id = input("Введите id книги, которую нужно удалить: ")
            try:
                book_id = int(book_id)
                library.delete_book(book_id)
                print(f"Книга с id {book_id} удалена")
            except ValueError:
                print("Ошибка: id должен быть числом")

        elif choice == "3":
            # Поиск книги
            search_by = input("Введите критерий поиска (title/author/year): ").strip()  # Считываем критерий поиска
            if search_by in ["title", "author", "year"]:  # Проверяем допустимые критерии поиска
                search_value = input(f"Введите значение для поиска по {search_by}: ").strip()  # Считываем значение для поиска
                if search_by == "year":
                    try:
                        search_value = int(search_value)  # Преобразуем значение в int, если критерий - год
                    except ValueError:
                        print("Год должен быть числом.")
                        continue
                books = library.search_books(search_by, search_value)  # Ищем книги по указанному критерию
                if books:
                    for book in books:
                        print(book)  # Выводим найденные книги
                else:
                    print("Книга не найдена.")
            else:
                print("Некорректный критерий поиска. Доступные критерии: title, author, year.")

        elif choice == '4':
            # Отображение всех книг
            books = library.display_books()
            for book in books:
                print(book)

        elif choice == '5':
            # Изменение статуса книги
            book_id = input("Введите id книги: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            try:
                book_id = int(book_id)
                result = library.update_status(book_id, new_status)
                if result:
                    print(result)
                else:
                    print("Книга с таким id не найдена.")
            except ValueError:
                print("Ошибка: id должен быть числом")

        elif choice == '6':
            # Выход из программы
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()  # Запуск основной функции main при запуске скрипта