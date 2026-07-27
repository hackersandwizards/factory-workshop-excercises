# Pricing-Service

Verwaltet Rabatt-Regeln und Gutschein-Codes, unabhaengig vom Cart-Service.
`validate_coupon()` prueft einen Code gegen den Bestellwert, `apply_discount()`
rechnet ihn auf einen Betrag an.

Aktuell komplett eigenstaendig — keine Verbindung zum Cart-Service.

## Ausfuehren

```bash
python pricing.py
```
