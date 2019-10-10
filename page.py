from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_element(by_locator).click()

    def hover_to(self, by_locator):
        element = self.wait_element(by_locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def assert_elem_text(self, by_locator, elem_text):
        element = self.wait_element(by_locator)
        assert element.text == elem_text

    def navigate_browser_back(self):
        self.driver.back()


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.python.org")


class BlogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.python.org/blogs/")
