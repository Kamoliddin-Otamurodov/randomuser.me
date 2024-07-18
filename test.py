import pytest
from randomuser import RandomUser
from pprint import pprint

def test_random_user():
    user = RandomUser()

    assert user.get_name_title() in ["Mr", "Mrs", "Ms", "Miss", "Dr"], "Invalid name title"
    assert isinstance(user.get_first_name(), str), "First name is not a string"
    assert isinstance(user.get_last_name(), str), "Last name is not a string"
    assert isinstance(user.get_full_name(), str), "Full name is not a string"
    assert "@" in user.get_email(), "Invalid email format"
    assert isinstance(user.get_phone(), str), "Phone number is not a string"
    assert isinstance(user.get_cell(), str), "Cell number is not a string"
    assert user.get_gender() in ["male", "female"], "Gender is invalid"
    assert len(user.get_nationality()) == 2, "Nationality should be a 2-letter code"