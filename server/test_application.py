import pytest
from application import TestMe

def test_take_five():
    """ Проверяет, что метод take_five возвращает 5 """
    assert TestMe().take_five() == 5

def test_port():
    """ Проверяет, что порт сервера равен 8000 """
    assert TestMe().port() == 8000
