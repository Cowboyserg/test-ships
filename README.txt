conftest.py - содержит фикстуры и хуки
delete_bd.py - скрипт для удаления баз данных
logic.py - содержит логику работы программы с информацией, полученной из баз данных
conf_help.py - нужен для правильной работы фикстуры из conftest
requirements.txt - содержит необходимые для работы пакеты
sql.py - для работы подключения и общения с базой данных
test_fixture.py - создание базы данных с рандомизированными значениями и проверка существования получившегося файла
test_two_bd.py - тест, сравнение двух баз данных

Запуск проекта:

Сначала убеждаемся в том, что нет баз данных, для этого запускаем delete_bd.py
Запускаем sql.py для создания первой базы данных
Далее запускаем тест test_dif из test_fixture.py для создания второй базы данных с рандомизированными значениями
После чего тест test из test_two_bd.py для сравнения получившихся баз данных