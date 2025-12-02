# tests/test_e2e.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument("--headless")  # mode headless
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()), options=options
    )
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def test_login_flow(browser):
    browser.get(BASE_URL + "/login")

    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.TAG_NAME, "button")

    username.send_keys("alice")
    password.send_keys("secret")
    submit.click()

    time.sleep(1)

    assert browser.current_url.endswith("/")


def test_create_task_from_ui(browser):
    browser.get(BASE_URL + "/tasks/new")

    title = browser.find_element(By.NAME, "title")
    description = browser.find_element(By.NAME, "description")
    submit = browser.find_element(By.TAG_NAME, "button")

    title.send_keys("Write Selenium test")
    description.send_keys("E2E test created via UI")
    submit.click()

    time.sleep(1)

    page_source = browser.page_source
    assert "Write Selenium test" in page_source


def test_toggle_task_from_ui(browser):
    browser.get(BASE_URL + "/")

    toggle_buttons = browser.find_elements(
        By.CSS_SELECTOR, "form[action*='toggle'] button"
    )

    assert len(toggle_buttons) > 0

    first_button = toggle_buttons[0]
    first_button.click()

    time.sleep(1)

    assert "Task status updated" in browser.page_source
