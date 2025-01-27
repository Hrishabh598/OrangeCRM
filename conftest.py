import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
USERNAME = "Admin"
PASS = "admin123"

@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    options = ChromeOptions()
    options.add_experimental_option("detach",True)
    request.cls.driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

