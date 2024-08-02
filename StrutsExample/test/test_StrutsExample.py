# test_StrutsExample.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_utils import driver, perform_test

def check_index(driver, url):
    """Check if the title contains 'Index'."""
    driver.get(url)
    # Wait until the title contains 'Index'
    WebDriverWait(driver, 10).until(EC.title_contains("Index"))
    assert "Index" in driver.title, "テスト失敗: タイトル'Index'の画面が表示されませんでした。"

def test_index(driver):
    url = 'http://localhost:8080/StrutsExample/'
    perform_test(driver, url, check_index)

def check_hello_world(driver, url):
    """Check if the body text contains 'Hello, World!'."""
    driver.get(url)
    # Wait until the body text contains 'Hello, World!'
    WebDriverWait(driver, 10).until(lambda d: "Hello, World!" in d.find_element(By.TAG_NAME, 'body').text)
    body_text = driver.find_element(By.TAG_NAME, 'body').text
    assert "Hello, World!" in body_text, "テスト失敗: 'Hello, World!'が表示されませんでした。"

def test_hello_world(driver):
    url = 'http://localhost:8080/StrutsExample/helloWorld.do'
    perform_test(driver, url, check_hello_world)
