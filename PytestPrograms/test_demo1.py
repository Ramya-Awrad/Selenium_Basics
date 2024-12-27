#Any pytest file name starts with test_ or _test
#pytest methods/funtions names start with test
#any code should be wrapped in method only
#method name should have sense
#to run it on cmnd prompt py.test -v -s run all files
#-k stands for method names execution(Regular expression), -s logs in output, -v stands for more info metadata
#you can run specific file py.test <filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
#you can skip tests with @pytest.mark.skip
#@pytest.mark.xfail
#fuxtures are used as setup and tear down methods for test cases - conftest file to generalize fixture
#fixture and make it available to all test cases
#datadriven and parameterization can be done with return statements in tuple format
#when you define fixture scope to class only, it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_greeting():
    print("Hello")

