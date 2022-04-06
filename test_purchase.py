import pytest

#teardown fiunction working in pytest


@pytest.fixture()
def setUp():    #setup will run before testcase like constructor
    # print("Setup started")
    print("user logged in.")
    #teardown function working in pytest
    yield      #it is like destructor it runs after testcases
    print("user logged out.")

def test_AddItemtoCart(setUp):
    print("Add item successfully")

def test_RemoveItemfromCart(setUp):
    print("Removed item successfully")

