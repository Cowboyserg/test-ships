# -*- coding: utf8 -*-
import os
import pytest


if __name__ == '__main__':
    """Удаляем все базы данных, если такие имеются"""
    for file in os.listdir():
        if ".db" in file:
            os.remove(file)