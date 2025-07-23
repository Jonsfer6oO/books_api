from enum import Enum

class Genre(str, Enum):
    genre_1 = 'fantasy'
    genre_2 = 'scientific'
    genre_3 = 'romance novel'

class Author(str, Enum):
    author_1 = 'Susi Fox'
    author_2 = 'Jone Monet'
    author_3 = 'Klon Green'
    author_4 = 'Sulan Guni'