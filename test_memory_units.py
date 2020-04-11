from memory_units import Unit, InvalidSuffix
import pytest


class TestUnitFromSuffix:
    def test_from_b_returns_bytes(self):
        suffix = "B"

        actual = Unit.from_suffix(suffix)
        expected = Unit.BASE

        assert actual == expected

    def test_from_gb_returns_giga(self):
        suffix = "GB"

        actual = Unit.from_suffix(suffix)
        expected = Unit.GIGA

        assert actual == expected

    def test_from_lowercase_mb_returns_mega(self):
        suffix = "mb"

        actual = Unit.from_suffix(suffix)
        expected = Unit.MEGA

        assert actual == expected

    def test_invalid_suffix_raises_error(self):
        suffix = "OB"

        with pytest.raises(InvalidSuffix) as error:
            Unit.from_suffix(suffix)
        print(error)
        error.match("Valid suffixes are")
