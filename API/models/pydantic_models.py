from pydantic import BaseModel, Field
from typing import Optional, Literal

class BookParams(BaseModel):
    id: Optional[int] = Field(None, le=10)
    genre: Literal['fantasy', 'scientific', 'romance novel'] = None
    authors: Literal['Susi Fox', 'Jone Monet', 'Klon Green', 'Sulan Guni'] = None
    pages: Optional[int] = Field(None, ge=200, le=500)
    chapters: Optional[int] = Field(None, ge=10, le=40)