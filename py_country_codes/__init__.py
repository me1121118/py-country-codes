from typing import Optional, Dict, List
from dataclasses import dataclass

@dataclass(frozen=True)
class Country:
    alpha2: str
    alpha3: str
    numeric: str
    name: str
    dial_code: str
    currency: str

    @property
    def flag(self) -> str:
        return country_to_flag(self.alpha2)

def country_to_flag(alpha2: str) -> str:
    """Convert an ISO 3166-1 alpha-2 code to a Unicode regional indicator flag emoji."""
    alpha2 = alpha2.strip().upper()
    if len(alpha2) != 2 or not alpha2.isalpha():
        return ""
    return chr(ord(alpha2[0]) + 127397) + chr(ord(alpha2[1]) + 127397)

COUNTRIES_DATA: List[Country] = [
    Country("US", "USA", "840", "United States", "+1", "USD"),
    Country("GB", "GBR", "826", "United Kingdom", "+44", "GBP"),
    Country("CA", "CAN", "124", "Canada", "+1", "CAD"),
    Country("AU", "AUS", "036", "Australia", "+61", "AUD"),
    Country("DE", "DEU", "276", "Germany", "+49", "EUR"),
    Country("FR", "FRA", "250", "France", "+33", "EUR"),
    Country("JP", "JPN", "392", "Japan", "+81", "JPY"),
    Country("CN", "CHN", "156", "China", "+86", "CNY"),
    Country("IN", "IND", "356", "India", "+91", "INR"),
    Country("BR", "BRA", "076", "Brazil", "+55", "BRL"),
    Country("TH", "THA", "764", "Thailand", "+66", "THB"),
    Country("SG", "SGP", "702", "Singapore", "+65", "SGD"),
    Country("VN", "VNM", "704", "Vietnam", "+84", "VND"),
    Country("ID", "IDN", "360", "Indonesia", "+62", "IDR"),
    Country("MY", "MYS", "458", "Malaysia", "+60", "MYR"),
    Country("KR", "KOR", "410", "South Korea", "+82", "KRW"),
    Country("NL", "NLD", "528", "Netherlands", "+31", "EUR"),
    Country("ES", "ESP", "724", "Spain", "+34", "EUR"),
    Country("IT", "ITA", "380", "Italy", "+39", "EUR"),
    Country("SE", "SWE", "752", "Sweden", "+46", "SEK"),
    Country("CH", "CHE", "756", "Switzerland", "+41", "CHF"),
    Country("NZ", "NZL", "554", "New Zealand", "+64", "NZD"),
    Country("MX", "MEX", "484", "Mexico", "+52", "MXN"),
    Country("AE", "ARE", "784", "United Arab Emirates", "+971", "AED"),
    Country("SA", "SAU", "682", "Saudi Arabia", "+966", "SAR"),
]

_BY_ALPHA2: Dict[str, Country] = {c.alpha2.upper(): c for c in COUNTRIES_DATA}
_BY_ALPHA3: Dict[str, Country] = {c.alpha3.upper(): c for c in COUNTRIES_DATA}
_BY_NAME: Dict[str, Country] = {c.name.lower(): c for c in COUNTRIES_DATA}

def get_country(query: str) -> Optional[Country]:
    """Lookup country by Alpha-2, Alpha-3, or English common name."""
    if not query:
        return None
    q = query.strip()
    q_upper = q.upper()
    if q_upper in _BY_ALPHA2:
        return _BY_ALPHA2[q_upper]
    if q_upper in _BY_ALPHA3:
        return _BY_ALPHA3[q_upper]
    return _BY_NAME.get(q.lower())

def list_countries() -> List[Country]:
    """Return all registered countries."""
    return list(COUNTRIES_DATA)
