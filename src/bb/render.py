import textwrap

from bb import BbError
from bb.books import Book
from bb.reference import Reference

BOLD, DIM, RESET = "\033[1m", "\033[2m", "\033[0m"


def render(book: Book, ref: Reference, width: int = 80, color: bool = False) -> str:
    chapters = book["chapters"]
    if ref.chapter > len(chapters):
        raise BbError(f"{book['name']} tem {len(chapters)} capítulos.")
    verses = chapters[ref.chapter - 1]

    start = ref.start or 1
    end = min(ref.end or len(verses), len(verses))
    if start > len(verses):
        raise BbError(f"{book['name']} {ref.chapter} tem {len(verses)} Versículos.")

    bold, dim, reset = (BOLD, DIM, RESET) if color else ("", "", "")
    title = f"{book['name']} {ref.chapter}"
    if ref.start is not None:
        title += f":{start}" if start == end else f":{start}-{end}"

    lines = [f"{bold}{title}{reset}", ""]

    for number in range(start, end + 1):
        prefix = f"{number:>3} "
        wrapped = textwrap.wrap(verses[number - 1], width - len(prefix))
        lines.append(f"{dim}{prefix}{reset}{wrapped[0]}")
        lines.extend(" " * len(prefix) + part for part in wrapped[1:])
    return "\n".join(lines)
