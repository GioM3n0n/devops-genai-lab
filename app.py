"""Exemplo didático: cálculo de frete com um erro intencional."""


def calculate_shipping(base_price: float, tax_rate: float | str) -> float:
    """Soma o preço-base e a taxa de frete.

    BUG INTENCIONAL: uma taxa recebida como string provoca TypeError.
    """
    return base_price + tax_rate  # type: ignore[operator]


if __name__ == "__main__":
    print(calculate_shipping(10.0, "2.5"))
