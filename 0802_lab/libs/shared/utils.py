"""Утилиты общей библиотеки."""

def format_greeting(name):
    return "Hello, %s!" % name

def slugify(text):
    return "-".join(text.strip().lower().split())
