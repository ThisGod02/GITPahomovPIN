"""Модуль авторизации (feature/login)."""

def authenticate(username, password):
    """Учебная проверка логина."""
    return username == "admin" and password == "secret"


def logout(session):
    """Завершение сессии (hotfix)."""
    session.clear()
