import logging
from typing import Annotated

from fastapi import APIRouter, HTTPException, status
from fastapi import Query, Path

import functions
from . import models

# По названию. 3 названия.
# По жанру. 3 жанра. Enum
# Поулчение книги по авторам. Всего 4 автора. Enum.
# По страницам. Больше какого-то значения.
# По количеству глав. Больше какого то значения.

db_logger = logging.getLogger(__name__)

db_logger.info('Создание роутера.')
db_router = APIRouter(
    prefix="/db/book",
    tags=['db']
)
db_logger.info('Роутер создан')

@db_router.get('/name/{name_book}',
               description='Getting a book by name.',
               status_code=status.HTTP_200_OK)
async def get_book_name(name_book: Annotated[str, Path(min_length=5, max_length=10)]):
    try:
        return functions.search_name(name_book)
    except Exception as ex:
        db_logger.error(f'Получение книги по имени. name_book={name_book}', exc_info=True)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=ex)

@db_router.get('/ganre/{ganre}',
               description='Getting books by genre.',
               status_code=status.HTTP_200_OK)
async def get_books_genre(genre: models.Genre):
    try:
        return functions.search_genre(genre)
    except Exception as ex:
        db_logger.error(f'Получение книг по жанру. genre={genre}', exc_info=True)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=ex)

@db_router.get('/author/{author}',
               description='Getting books by author.',
               status_code=status.HTTP_200_OK)
async def get_books_author(author: models.Author):
    try:
        return functions.search_author(author)
    except Exception as ex:
        db_logger.error(f'Получение книг по автору. author={author}', exc_info=True)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=ex)

@db_router.get('/pages/{pages}',
               description='Getting books by pages larger than in "pages".',
               status_code=status.HTTP_200_OK)
async def get_books_pages(pages: Annotated[int, Path(ge=200, le=700)]):
    try:
        return functions.search_pages(pages)
    except Exception as ex:
        db_logger.error(f'Получение книг по количеству страниц. pages={pages}', exc_info=True)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=ex)

@db_router.get('/chapters/{chapters}',
               description='Getting books by chapters larger than "chapters".',
               status_code=status.HTTP_200_OK)
async def get_books_chapters(chapters: Annotated[int, Path(ge=10, le=40)]):
    try:
        return functions.search_chapters(chapters)
    except Exception as ex:
        db_logger.error(f'Получение книг по количеству глав. chapters={chapters}', exc_info=True)
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=ex)