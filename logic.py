# -*- coding: utf8 -*-
from sql import Sql


def get_db(name:str) -> list:
    """Возвращает список, в котором информация из указанной базы данных"""
    mas_all = []
    dic = {}
    base = Sql(name)
    tables_tuple = base.get_all_tables()
    tables_mas = [list(i) for i in tables_tuple]
    for i in tables_mas:
        # убираем из подписей все лишнее
        table_name = i[0]
        podpisi = base.get_table_names(table_name)
        podpisi = [list(x)[1] for x in podpisi]
        inf = base.get_table_inf_by_name(table_name)
        inf = [list(x) for x in inf]
        # собираем информацию и подписи и записываем в inf
        if "ships" not in table_name:
            for j in range(len(inf)):
                for k in range(1, len(inf[j])):
                    inf[j][k] = {podpisi[k]: inf[j][k]}
        mas_all.append(inf)
    ships = mas_all[-1]
    not_ships = mas_all[:-1]
    dic_not_ships = {}
    for i in range(len(not_ships)):
        for j in range(len(not_ships[i])):
            dic_not_ships[not_ships[i][j][0]] = not_ships[i][j][1:]

    for i in range(len(ships)):
        dic[ships[i][0]] = {ships[i][1]: dic_not_ships[ships[i][1]],
                            ships[i][2]: dic_not_ships[ships[i][2]],
                            ships[i][3]: dic_not_ships[ships[i][3]]}
    # преобразуем получившийся словарь в двумерный список, который можно поместить в параметризацию
    mas_out = []
    for key, value in dic.items():
        for key1, value1 in value.items():
            for param in value1:
                for key2, value2 in param.items():
                    mas = [key, key1, key2, value2]
                    mas_out.append(mas)
    return mas_out


def delete_extra(mas1:list, mas2:list) -> tuple:
    """Удаляет лишние данные из списков"""
    dic = {}
    mas_skip = []
    for i in range(len(mas1)):
        if i not in mas_skip:
            if mas1[i][1] != mas2[i][1]:
                skip = [mas1[i][0], mas1[i][1]]
                for j in range(i + 1, len(mas1)):
                    if [mas1[j][0], mas1[j][1]] == skip:
                        mas_skip.append(j)
                    else:
                        break
    mas1_new = []
    mas2_new = []
    for i in range(len(mas1)):
        if i not in mas_skip:
            mas1_new.append(mas1[i])
            mas2_new.append(mas2[i])
    return mas1_new, mas2_new

# название корабля, название компонента, название параметра, параметр компонента
def two_lists_in_one(mas1:list, mas2:list) -> list:
    """Совмещает списки двух баз данных в одно целое для помещения в тест"""
    mas1, mas2 = delete_extra(mas1, mas2)
    for i in range(len(mas1)):
        for j in range(len(mas2[i])):
            mas1[i].append(mas2[i][j])
    return mas1


if __name__ == '__main__':
    print(get_db("Wargaming.db"))
    print(get_db("Wargaming_bad.db"))