import inspect

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from GenericUtil import configure_log, configration_file_reader, global_variables
from GenericUtil.generic_util import generate_bat_file
import allure
from allure_commons.types import AttachmentType
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser options : chrome or firefox or edge or opera"
    )


@pytest.fixture()
def setup(request):
    # generate_bat_file()
    global driver
    browser_name = request.config.getoption("--browser_name")
    log = configure_log.get_logger_instance()
    if str(browser_name).lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        log.info("Initializing Chrome browser")
    elif str(browser_name).lower() == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        log.info("Initializing Firefox browser")
    elif str(browser_name).lower() == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        log.info("Initializing Edge browser")
    elif str(browser_name).lower() == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        log.info("Initializing Opera browser")
    driver.get(global_variables.uat_env_url)

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="../Screenshots"+inspect.stack()[1][3], attachment_type=AttachmentType.PNG)
    driver.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

# @pytest.fixture()
# def log_on_failure(request,):
#     yield
#     item = request.node
#     driver = setup
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)
