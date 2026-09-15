# py-country-codes

[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-blue.svg)](https://pypi.org/project/py-country-codes/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Zero-dependency ISO-3166-1 country code lookup, flag emoji converter, dial calling codes, and currency codes in pure Python.

---

## 🚀 Features

- 🪶 **Zero Dependencies**: Pure Python standard library.
- 🌐 **ISO-3166-1 Compliant**: Lookup by Alpha-2 (`US`), Alpha-3 (`USA`), or common English name (`United States`).
- 🚩 **Flag Emoji Generator**: Algorithmic conversion from Alpha-2 country code to official Unicode flag emoji (e.g., `TH` -> `🇹🇭`).
- 📞 **Calling Codes**: International telephone prefix lookup (e.g., `+66`, `+1`).
- 💰 **Currency Codes**: Associated primary currency code (e.g., `THB`, `USD`, `EUR`).

---

## 📦 Installation

```bash
pip install py-country-codes
```

---

## 🛠️ Quickstart

```python
from py_country_codes import get_country, country_to_flag

# 1. Lookup Country
th = get_country("TH")
print(th.name)         # Thailand
print(th.alpha3)       # THA
print(th.dial_code)    # +66
print(th.currency)     # THB
print(th.flag)         # 🇹🇭

# 2. Flag Emoji Utility
print(country_to_flag("JP"))  # 🇯🇵
print(country_to_flag("GB"))  # 🇬🇧
```

---

## ☕ Support My Studies / Buy Me a Coffee

I am an independent developer and student building open-source developer productivity tools. If this library simplified your internationalization or country dropdown logic, please consider supporting my studies:

- ☕ **Buy Me a Coffee:** [buymeacoffee.com/kcidi4148](https://buymeacoffee.com/kcidi4148)
- ⭐ **Star this repository** on GitHub!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
