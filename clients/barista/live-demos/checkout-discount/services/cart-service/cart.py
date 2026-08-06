"""Cart-Service: manages shopping carts and the checkout flow.

Current state: checkout only calculates the plain item total.
Discount codes and coupons are not taken into account yet.
"""

from dataclasses import dataclass, field


@dataclass
class LineItem:
    sku: str
    name: str
    unit_price_cents: int
    quantity: int

    @property
    def subtotal_cents(self) -> int:
        return self.unit_price_cents * self.quantity


@dataclass
class Cart:
    cart_id: str
    items: list[LineItem] = field(default_factory=list)

    def add_item(self, item: LineItem) -> None:
        self.items.append(item)

    def raw_total_cents(self) -> int:
        return sum(item.subtotal_cents for item in self.items)

    def checkout(self) -> dict:
        """Closes the cart and returns the payment summary.

        TODO: discount codes and coupons are not applied here yet.
        The Pricing-Service (see ../pricing-service/) already manages the
        discount rules, but is not wired up.
        """
        return {
            "cart_id": self.cart_id,
            "item_count": len(self.items),
            "total_cents": self.raw_total_cents(),
        }


if __name__ == "__main__":
    cart = Cart(cart_id="demo-cart-1")
    cart.add_item(LineItem(sku="COFFEE-001", name="Barista Blend 500g", unit_price_cents=899, quantity=2))
    cart.add_item(LineItem(sku="MUG-042", name="Barista Mug", unit_price_cents=650, quantity=1))
    print(cart.checkout())
