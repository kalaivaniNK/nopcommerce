import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        return driver
    else:
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#pytest html report
#it is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['module Name'] = 'Customers'
    config._metadata['Tester'] = 'pradeep'

#it is hook for delete/modify environment info to html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
    # metadata.pop("JAVA_HOME", None)
    # metadata.pop("Plugins", None)
    # metadata.pop("Packages", None)
    # metadata.pop("Platform", None)