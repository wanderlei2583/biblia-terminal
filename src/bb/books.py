from typing import TypedDict

from bb import BbError


class Book(TypedDict):
    abbrev: str
    name: str
    chapters: list[list[str]]


ALIASES = {"job": "jó", "at": "atos", "sal": "sl"}


def find_book(bible: list[Book], abbrev: str) -> Book:
    key = ALIASES.get(abbrev, abbrev)
    for book in bible:
        if book["abbrev"] == key:
            return book
    raise BbError(f"Livro '{abbrev}' não encontrado. Rode 'bb' para ver a lista.")
