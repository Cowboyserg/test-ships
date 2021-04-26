# -*- coding: utf8 -*-
import pytest
from logic import *
from random import randint
from conf_help import get_good_dic


@pytest.fixture(scope='session')
def make_bad_dic(name="Wargaming_bad.db"):
    """Создает вторую базу данных и возвращает информацию из этой базы"""
    bad_name = name
    dic_good = get_good_dic()
    dic_bad = dic_good
    for key, value in dic_bad.items():
        mas = [list(i) for i in value]
        if key == "ships":
            v = 200
            for i in range(len(mas)):
                r = randint(1, len(mas[i]) - 1)  # случайный номер элемента
                p1, p2 = mas[i][r].split("-")
                if "Weapon" in p1:
                    p2 = randint(1, 20)
                elif "Hull" in p1:
                    p2 = randint(1, 5)
                elif "Engine" in p1:
                    p2 = randint(1, 6)
                mas[i][r] = p1 + "-" + str(p2)
        elif key == "weapons":
            v = 20
        elif key == "hulls":
            v = 5
        elif key == "engines":
            v = 6
        if key != "ships":
            for i in range(len(mas)):
                r = randint(1, len(mas[i]) - 1)
                mas[i][r] = randint(1, v)
        dic_bad[key] = mas
    # создание плохой базы данных
    base_bad = Sql(bad_name)
    base_bad.create_tables()
    for key, value in dic_bad.items():
        if key == "weapons":
            for i in value:
                base_bad.exec_custom_command1(f"INSERT INTO {key.lower()} (weapon, "
                                              f"'reload speed', 'rotation speed', diametr, 'power volley', count) "
                                              f"VALUES ('{i[0]}',{i[1]},{i[2]},{i[3]},{i[4]},{i[5]})")
        elif key == "hulls":
            for i in value:
                base_bad.exec_custom_command1(
                    f"INSERT INTO {key} (hull, armor, type, capacity) VALUES ('{i[0]}',{i[1]},{i[2]},{i[3]})")
        elif key == "engines":
            for i in value:
                base_bad.exec_custom_command1(
                    f"INSERT INTO {key} (engine, power, type) VALUES ('{i[0]}',{i[1]},{i[2]})")
        elif key == "ships":
            for i in value:
                base_bad.exec_custom_command1(
                    f"INSERT INTO {key} (ship, weapon, hull, engine) VALUES ('{i[0]}','{i[1]}','{i[2]}','{i[3]}')")

# def test_dif(make_bad_dic):
#     print(123)