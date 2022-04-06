import pytest

@pytest.fixture()
def setUp():
    print("Setup started")

def test_AddItemtoCart(setUp):
    print("Add item successfully")

def test_RemoveItemfromCart(setUp):
    print("Removed item successfully")

