import pytest


# @pytest.fixture(scope="module", autouse=True)
# @pytest.fixture(scope="package", autouse=True)
@pytest.fixture(scope="session", autouse=True)
# @pytest.fixture(scope="function", autouse=True)  this is by default
def tc_setUp(browser):
    if browser == "chrome":
        print("Launch Browser")
    elif browser == "ff":
        print("Launch Fire Fox")
    else:
        print("Provide a valid browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Browser Close")


def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addoption("--platform")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
