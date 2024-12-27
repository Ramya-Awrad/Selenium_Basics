import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will executing first")
    yield
    print("i will execute last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Ramya", "Awrad","ramyaawrad.com"]
