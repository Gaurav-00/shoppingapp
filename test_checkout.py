import pytest

@pytest.fixture()
def setUp():
    print("Open my amazon app")
    print("user logged in.")
    # teardown function working in pytest
    yield  # it is like destructor it runs after testcases
    print("user logged out.")
    print("Close amazon app")

def test_checkOut(setUp):
    print("Made payment successfully.")
