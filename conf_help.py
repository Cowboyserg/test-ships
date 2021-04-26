# -*- coding: utf8 -*-
from sql import Sql
import pytest


def get_good_dic() -> dict:
    """Возвращает словарь с информацией из первой (хорошей) базы данных"""
    dic_good = {}
    # получаем информацию из нормальной базы данных
    base_good = Sql("Wargaming.db")
    tables_names = base_good.get_all_tables()
    tables_names = [list(i) for i in tables_names]
    for i in tables_names:
        inf = base_good.exec_custom_command(f'SELECT * FROM {i[0]}')
        inf = [list(i) for i in inf]
        dic_good[i[0]] = inf
    return dic_good

