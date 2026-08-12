from typing import list, tuple, dict, union


age: int = 25

def greeting(name: str) -> str:
    return f"Hello, {name}!"


numbers: list[int] = [1, 2, 3, 4, 5]

person: tuple[str, int] = ("Sanju", 18)

scores: dict[str, int] = {"Sanju": 18, "Rishav": 20}

indentifier: union[int, str] = "ID123"
identifier = 12345
