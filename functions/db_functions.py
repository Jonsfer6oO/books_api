import logging
from typing import Union

from db import database as db

funcs_logger = logging.getLogger(__name__)

def search_name(name: str) -> dict:
    try:
        return db.get(name, {})
    except:
        funcs_logger.error(f'Поиск по имени. name={name}', exc_info=True)
        return {}

def search_genre(genre: str) -> Union[dict[str, dict], dict]:
    try:
        book: dict
        dict_books = {}

        for name_book in db:
            book = db[name_book]
            if book.get('genre') == genre:
                dict_books[name_book] = book

        return dict_books
    except:
        funcs_logger.error(f'Поиск по жанру. genre={genre}', exc_info=True)
        return {}

def search_author(author: str) -> Union[dict[str, dict], dict]:
    try:
        book: dict
        dict_books = {}

        for name_book in db:
            book = db[name_book]
            if author in book.get('authors'):
                dict_books[name_book] = book

        return dict_books
    except:
        funcs_logger.error(f'Поиск по жанру. author={author}', exc_info=True)
        return {}

def search_pages(pages: int) -> Union[dict[str, dict], dict]:
    try:
        book: dict
        dict_books = {}

        for name_book in db:
            book = db[name_book]
            if pages >= book.get('pages'):
                dict_books[name_book] = book

        return dict_books
    except:
        funcs_logger.error(f'Поиск по страницам. pages={pages}', exc_info=True)
        return {}

def search_chapters(chapters: int) -> Union[dict[str, dict], dict]:
    try:
        book: dict
        dict_books = {}

        for name_book in db:
            book = db[name_book]
            if chapters >= book.get('chapters'):
                dict_books[name_book] = book

        return dict_books
    except:
        funcs_logger.error(f'Поиск по жанру. chapters={chapters}', exc_info=True)
        return {}
