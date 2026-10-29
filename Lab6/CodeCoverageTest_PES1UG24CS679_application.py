
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# Ticket price tests

def test_unknown_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("invalid", 25, 15, False)


def test_show_hour_below_zero():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_show_hour_above_23():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_morning_discount():
    assert ticket_price("regular", 25, 10, False) == 100


def test_afternoon_regular_ticket():
    assert ticket_price("regular", 25, 15, False) == 150


def test_evening_premium_ticket():
    assert ticket_price("premium", 25, 18, False) == 280


def test_weekend_extra_charge():
    assert ticket_price("regular", 25, 15, True) == 190


def test_child_under_three():
    assert ticket_price("recliner", 2, 20, True) == 0


def test_child_discount():
    assert ticket_price("regular", 12, 15, False) == 75


def test_senior_citizen_discount():
    assert ticket_price("premium", 60, 15, False) == 125


# Group discount tests

def test_zero_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_negative_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(-1, False)


def test_group_of_ten():
    assert group_discount(10, False) == 15


def test_group_of_five():
    assert group_discount(5, False) == 10


def test_small_group():
    assert group_discount(2, False) == 0


def test_student_group_with_large_discount():
    assert group_discount(10, True) == 20


def test_student_group_with_medium_discount():
    assert group_discount(5, True) == 15


def test_student_group_without_discount():
    assert group_discount(2, True) == 0


# Snack combo tests

def test_small_snack_with_coupon():
    assert snack_combo("small", True) == 70


def test_small_snack_without_coupon():
    assert snack_combo("small", False) == 120


def test_medium_snack_without_coupon():
    assert snack_combo("medium", False) == 180


def test_medium_snack_with_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack_without_coupon():
    assert snack_combo("large", False) == 250


def test_other_snack_size_with_coupon():
    assert snack_combo("large", True) == 200
