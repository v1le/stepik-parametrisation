import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--lang', action='store', default=None, help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    browser = request.config.getoption('browser')
    user_language = request.config.getoption('lang')
    if browser == 'chrome':
        print('\nstart chrome browser for test..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        print('\nstart firefox browser for test..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('choose language to run tests')
    yield browser
    browser.quit()