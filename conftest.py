from datetime import datetime
from pathlib import Path
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

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("hrm_reports",today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True,exist_ok=True)
    pytest_html = report_dir/f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Orange CRM Test Report"