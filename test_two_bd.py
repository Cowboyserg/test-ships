# -*- coding: utf8 -*-
import pytest
from logic import two_lists_in_one, get_db


@pytest.mark.parametrize("f1, f2, f3, f4, f5, f6, f7, f8", two_lists_in_one(get_db("Wargaming.db"),
                                                                            get_db("Wargaming_bad.db")))
def test(f1, f2, f3, f4, f5, f6, f7, f8):
    """Сравниваем две получившиеся базы данных"""
    if f2 != f6:
        # изменилось орудие, корпус или двигатель
        assert f2 == f6, f"\n{f1}, {f6}\n\texpected {f2}, was {f6}"
    elif f2 == f6:
        # значение параметра компонента не соответствует тому, что было
        assert f4 == f8, f"\n{f1}, {f2}\n\t{f3}: expected {f4}, was {f8}"