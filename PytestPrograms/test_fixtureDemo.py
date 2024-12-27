import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_Demo(self):
        print("i will execute after fixture")

    def test_Demo1(self):
        print("i will execute after demo1 fixture")

    def test_Demo2(self):
        print("i will execute after demo2 fixture")

    def test_Demo3(self):
        print("i will execute after demo3 fixture")
