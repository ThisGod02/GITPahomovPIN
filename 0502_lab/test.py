#!/usr/bin/env python3
"""Тестовый модуль для проверки CI/CD."""

def test_addition():
    """Тест сложения."""
    assert 1 + 1 == 2
    print("test_addition passed")

def test_subtraction():
    """Тест вычитания."""
    assert 2 - 1 == 1
    print("test_subtraction passed")

if __name__ == "__main__":
    print("Running tests...")
    test_addition()
    test_subtraction()
    print("All tests passed!")
