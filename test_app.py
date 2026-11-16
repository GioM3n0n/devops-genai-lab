"""Testes unitários da aplicação."""

from app import calculate_shipping


def test_calculate_shipping():
    """Este teste deve falhar até a correção do BUG intencional."""
    assert calculate_shipping(10.0, "2.5") == 12.5


def test_calculate_shipping_numeric_rate():
    """Este teste deve passar com taxa já numérica."""
    assert calculate_shipping(10.0, 2.5) == 12.5
