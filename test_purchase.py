import pytest

#teardown fiunction working in pytest


@pytest.fixture()
def setUp():
    print("Setup started")
    # teardown fiunction working in pytest
    yield
    print("exited")

def test_AddItemtoCart(setUp):
    print("Add item successfully")

def test_RemoveItemfromCart(setUp):
    print("Removed item successfully")

