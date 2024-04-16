import pytest
import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from module import Site
from selenium import webdriver

with open('datatest.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    browser_name = data['browser']

@pytest.fixture(scope='session')
def browser():
    if browser_name == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def set_locator1():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def set_locator2():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def set_locator3():
    return '''button'''


@pytest.fixture()
def set_locator4():
    return '''h2'''


@pytest.fixture()
def status_error():
    return '401'


@pytest.fixture()
def site():
    site_instance = Site(data['address'])
    yield site_instance
    site_instance.quit()


# Новая фикстура для предоставления данных для нового шага в тесте
@pytest.fixture()
def post_data():
    return {
        "title": "New Post Title",
        # Дополнительные данные для поста, если нужно
    }


@pytest.fixture()
def input_username():
    return '''h2'''


@pytest.fixture()
def post_button_locator():
    return '#create-btn'


@pytest.fixture()
def find_title():
    return '''//*[@id="create-item"]/div/div/div[7]/div/button/span'''


@pytest.fixture()
def login_success():
    return '''//*[@id="app"]/main/nav/a/span'''


@pytest.fixture()
def create_post_button_locator():
    return '#create-item > div > div > div:nth-child(7) > div > button > span'


@pytest.fixture(scope='session')
def auth_token():
    address = data['address']
    payload = {
        "username": data['username'],
        "password": data['password']
    }
    try:
        # Отправка POST запроса для авторизации и получение токена
        response = requests.post(login_url, json=payload)
        response.raise_for_status()  # Проверка статус кода ответа
        token = response.json().get('token')  # Получение токена из ответа
        return token
    except requests.exceptions.RequestException as e:
        # Обработка ошибок при запросе авторизации
        pytest.fail(f"Failed to authenticate: {e}")