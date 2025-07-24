import logging
from typing import Union

from . import other
from db import database as db
from API.models import BookParams

funcs_logger = logging.getLogger(__name__)

class Search_methods:
    @staticmethod
    def search_name(name: str) -> dict:
        try:
            funcs_logger.info('Начало поиска книги по имени')
            funcs_logger.debug(f'name={name}')
            book = db.get(name, {})
            funcs_logger.debug(f'book={book}')
            funcs_logger.info('Конец поиска книги по имени')

            return book
        except:
            funcs_logger.error(f'Поиск по имени. name={name}', exc_info=True)
            return {}

    @staticmethod
    def search_genre(genre: str) -> Union[dict[str, dict], dict]:
        try:
            funcs_logger.info('Начало поиска книг по жанру')
            funcs_logger.debug(f'genre={genre}')

            book: dict
            dict_books = {}

            for name_book in db:
                book = db[name_book]
                funcs_logger.debug(f'Получена книга: name_book={name_book}, book={book}')
                if book.get('genre') == genre:
                    funcs_logger.debug('Сработало условие соотвествия жанра')
                    dict_books[name_book] = book
                    funcs_logger.debug('Книга добавлена в итоговый словарь')

            funcs_logger.info('Конец поиска книг по жанру')
            return dict_books
        except:
            funcs_logger.error(f'Поиск по жанру. genre={genre}', exc_info=True)
            return {}

    @staticmethod
    def search_author(author: str) -> Union[dict[str, dict], dict]:
        try:
            funcs_logger.info('Начало поиска книг по автору')
            funcs_logger.debug(f'author={author}')

            book: dict
            dict_books = {}

            for name_book in db:
                book = db[name_book]
                funcs_logger.debug(f'Поулчена книга: name_book={name_book}, book={book}')
                if author in book.get('authors'):
                    funcs_logger.debug('Сработало условие на наличие автора у книги')
                    dict_books[name_book] = book
                    funcs_logger.debug('Книга добавлена в итоговый словарь')

            funcs_logger.info('Конец поиска книг по автору')
            return dict_books
        except:
            funcs_logger.error(f'Поиск по жанру. author={author}', exc_info=True)
            return {}

    @staticmethod
    def search_pages(pages: int) -> Union[dict[str, dict], dict]:
        try:
            funcs_logger.info(f'Начало поиска книг по страницам')
            funcs_logger.debug(f'pages={pages}')

            book: dict
            dict_books = {}

            for name_book in db:
                book = db[name_book]
                funcs_logger.debug(f'Получена книга: name_book{name_book}, book={book}')
                if pages >= book.get('pages'):
                    funcs_logger.debug('Сработало условие наличия большего или равного числа страниц')
                    dict_books[name_book] = book
                    funcs_logger.debug('Книга добавлена в итоговый словарь')

            funcs_logger.info('Конец поиска книг по страницам')
            return dict_books
        except:
            funcs_logger.error(f'Поиск по страницам. pages={pages}', exc_info=True)
            return {}

    @staticmethod
    def search_chapters(chapters: int) -> Union[dict[str, dict], dict]:
        try:
            funcs_logger.info('Начало поиска по количеству глав')
            funcs_logger.debug(f'chapters={chapters}')

            book: dict
            dict_books = {}

            for name_book in db:
                book = db[name_book]
                funcs_logger.debug(f'Получена книга: name_book={name_book}, book={book}')
                if chapters >= book.get('chapters'):
                    funcs_logger.debug(f'Сработало условия наличия большего или равного числа глав')
                    dict_books[name_book] = book
                    funcs_logger.debug('Книга добавлена в итоговый словарь')

            funcs_logger.info('Конец поиска книг по главм')
            return dict_books
        except:
            funcs_logger.error(f'Поиск по жанру. chapters={chapters}', exc_info=True)
            return {}

    @staticmethod
    def serach_params(params: BookParams) -> Union[dict[str, dict], dict]:
        try:
            funcs_logger.info(f'Начало поиска книг по параметрам.')
            funcs_logger.debug(f'params={params.__dict__}')

            book: dict
            dict_books = {}

            for name_book in db:
                book = db[name_book]
                funcs_logger.debug(f'Получена книга. book={book}')

                for key, value in book.items():
                    param = other.getattr_validate(params, key)
                    funcs_logger.debug(f'Считано поле книги: key={key}, value={value}')
                    funcs_logger.debug(f'Считано поле класса: param={param}')

                    if param is None:
                        funcs_logger.debug('Сработало условие для None')
                        continue
                    elif isinstance(param, str) and param == value:
                        funcs_logger.debug('Сработало условие для str')
                        continue
                    elif isinstance(param, list) and param in value:
                        funcs_logger.debug('Сработало условие для списка')
                        continue
                    elif isinstance(param, int) and param <= value:
                        funcs_logger.debug('Сработало условие для числа')
                        continue
                    break
                else:
                    dict_books[name_book] = book
                    funcs_logger.debug(f'Книга добавлена в итоговый словарь')

            funcs_logger.info(f'Конец поиска книг по параметрам')
            return dict_books

        except:
            funcs_logger.error(f'Поиск по параметрам. params={params.__dict__}',exc_info=True)
            return {}