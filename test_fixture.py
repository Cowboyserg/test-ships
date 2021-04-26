# -*- coding: utf8 -*-
import os
import pytest


def test_dif(make_bad_dic):
    """Создаем новую базу данных и проверяем ее наличие"""
    assert "Wargaming_bad.db" in os.listdir()