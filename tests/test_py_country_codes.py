import pytest
from py_country_codes import get_country, country_to_flag, list_countries

def test_country_lookups():
    # Alpha-2 lookup
    th = get_country("TH")
    assert th is not None
    assert th.name == "Thailand"
    assert th.alpha3 == "THA"
    assert th.dial_code == "+66"
    assert th.currency == "THB"
    assert th.flag == "🇹🇭"

    # Alpha-3 lookup
    jp = get_country("JPN")
    assert jp is not None
    assert jp.alpha2 == "JP"
    assert jp.dial_code == "+81"

    # Name lookup (case-insensitive)
    us = get_country("united states")
    assert us is not None
    assert us.alpha2 == "US"
    assert us.currency == "USD"

def test_flag_emoji_conversion():
    assert country_to_flag("TH") == "🇹🇭"
    assert country_to_flag("jp") == "🇯🇵"
    assert country_to_flag("invalid") == ""

def test_list_countries():
    all_c = list_countries()
    assert len(all_c) >= 20
