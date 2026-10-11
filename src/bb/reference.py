from dataclasses import dataclass

from bb import BbError


@dataclass(frozen=True)
class Reference:
    book: str
    chapter: int
    start: int | None = None
    end: int | None = None


def _to_int(value: str, what: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise BbError(f"{what} precisa ser um número: '{value}'") from None
    if number < 1:
        raise BbError(f"{what} precisa ser maior que zero.")
    return number


def parse(book: str, numbers: list[str]) -> Reference:
    if not numbers:
        raise BbError("Informe ao menos o capítulo. Ex: bb gn 1")
    if len(numbers) > 3:
        raise BbError("Use no máximo: libro capítulo início fim")

    chapter = _to_int(numbers[0], "Capítulo")
    start = _to_int(numbers[1], "Versículo") if len(numbers) > 1 else None
    end = _to_int(numbers[2], "Versículo") if len(numbers) > 2 else start
    if start is not None and end is not None and start > end:
        start, end = end, start
    return Reference(book.lower(), chapter, start, end)
