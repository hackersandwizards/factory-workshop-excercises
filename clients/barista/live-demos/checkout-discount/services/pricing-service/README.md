# Pricing-Service

Manages discount rules and coupon codes, independently of the Cart-Service.
`validate_coupon()` checks a code against the order total, `apply_discount()`
applies it to an amount.

Currently fully standalone — no connection to the Cart-Service.

## Run

```bash
python pricing.py
```
