# -*- coding: utf8 -*-
import sqlite3
from random import randint


class Sql:
    def __init__(self, name):
        self.name = name
        self.connect = sqlite3.connect(name)
        self.cursor = self.connect.cursor()

    def create_tables(self):
        w_base = Sql(self.name)
        w_base.exec_custom_command("CREATE TABLE engines (engine TEXT (50) PRIMARY KEY,"
                                   "power INTEGER (50),"
                                   "type INTEGER (50))")

        w_base.exec_custom_command("CREATE TABLE weapons (weapon TEXT (50) PRIMARY KEY,"
                                   "'reload speed' INTEGER (50),"
                                   "'rotation speed' INTEGER (50),"
                                   "diametr INTEGER (50),"
                                   "'power volley' INTEGER (50),"
                                   "count INTEGER (50))")

        w_base.exec_custom_command("CREATE TABLE hulls (hull TEXT (50) PRIMARY KEY,"
                                   "armor INTEGER (50),"
                                   "type INTEGER (50),"
                                   "capacity INTEGER (50))")

        w_base.exec_custom_command("CREATE TABLE ships (ship TEXT (50) PRIMARY KEY,"
                                   "weapon TEXT (50) REFERENCES weapons (weapon),"
                                   "hull TEXT (50) REFERENCES hulls (hull),"
                                   "engine TEXT (50) REFERENCES engines (engine))")

    def get_table_inf_by_name(self, name):
        with self.connect:
            return self.cursor.execute("SELECT * FROM %s" % (name)).fetchall()

    def get_table_names(self, name):
        with self.connect:
            return self.cursor.execute("pragma table_info(%s)" % (name)).fetchall()

    def exec_custom_command(self, command):
        with self.connect:
            return self.cursor.execute(command).fetchall()

    def exec_custom_command1(self, command):
        with self.connect:
            return self.cursor.execute(command)

    def make_random_values_for_hulls(self):
        for i in range(1, 6):
            self.exec_custom_command("INSERT INTO hulls (hull,armor,type, capacity) "
                                     f"VALUES ('Hull-{i}', {randint(1, 20)}, {randint(1, 20)}, {randint(1, 20)})")

    def make_random_values_for_engines(self):
        for i in range(1, 7):
            self.exec_custom_command("INSERT INTO engines (engine,power,type) "
                                     f"VALUES ('Engine-{i}', {randint(1, 20)}, {randint(1, 20)})")

    def make_random_values_for_ships(self):
        for i in range(1, 201):
            self.exec_custom_command("INSERT INTO ships (ship, weapon,hull,engine) "
                                     f"VALUES ('Ship-{i}', 'Weapon-{randint(1, 20)}', 'Hull-{randint(1, 5)}',"
                                     f" 'Engine-{randint(1, 6)}')")

    def make_random_values_for_weapons(self):
        for i in range(1, 21):
            self.exec_custom_command("INSERT INTO weapons (weapon,'reload speed','rotation speed', diametr, "
                                     f"'power volley', count) VALUES ('Weapon-{i}', {randint(1, 20)}, {randint(1, 20)},"
                                     f" {randint(1, 20)}, {randint(1, 20)}, {randint(1, 20)})")

    def get_all_tables(self):
        with self.connect:
            return self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()


def sql_to_str(sql):
    return str(sql).replace("(", "").replace(",)", "").replace("'", "").replace("[", "").replace("]", "")


if __name__ == "__main__":
    # создаем и заполняем базу данных, которая без ошибок
    base = Sql("Wargaming.db")
    base.create_tables()
    base.make_random_values_for_weapons()
    base.make_random_values_for_hulls()
    base.make_random_values_for_engines()
    base.make_random_values_for_ships()
