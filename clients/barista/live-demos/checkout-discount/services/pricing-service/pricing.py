"""Pricing-Service: manages discount rules and coupon codes.

Current state: the discount logic exists and works standalone, but is not
connected to the Cart-Service anywhere.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class DiscountRule:
    code: str
    percent_off: int
    valid_until: date
    min_order_cents: int = 0

    def is_valid(self, order_total_cents: int, today: date) -> bool:
        return today <= self.valid_until and order_total_cents >= self.min_order_cents


_ACTIVE_RULES: dict[str, DiscountRule] = {
    "WELCOME10": DiscountRule(code="WELCOME10", percent_off=10, valid_until=date(2026, 12, 31)),
    "KAFFEE20": DiscountRule(code="KAFFEE20", percent_off=20, valid_until=date(2026, 9, 30), min_order_cents=2000),
}


def validate_coupon(code: str, order_total_cents: int, today: date | None = None) -> DiscountRule | None:
    """Checks a coupon code against the current order total.

    Returns the matching rule, or None if the code is invalid, expired, or
    the minimum order value has not been reached.
    """
    today = today or date.today()
    rule = _ACTIVE_RULES.get(code.upper())
    if rule is None or not rule.is_valid(order_total_cents, today):
        return None
    return rule


def apply_discount(order_total_cents: int, rule: DiscountRule) -> int:
    discount_cents = (order_total_cents * rule.percent_off) // 100
    return order_total_cents - discount_cents


if __name__ == "__main__":
    rule = validate_coupon("KAFFEE20", order_total_cents=2448)
    print(rule, apply_discount(2448, rule) if rule else None)
