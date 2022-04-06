import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("Open my amazon app")
    print("user logged in.")
    # teardown function working in pytest
    yield  # it is like destructor it runs after testcases
    print("user logged out.")
    print("Close amazon app")