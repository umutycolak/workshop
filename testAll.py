import unittest

from selenium import webdriver
from page import HomePage
from page import BlogPage
from locators import CommonPageLocators
from locators import BlogPageLocators


class TestPyOrgBase(unittest.TestCase):
    """
    TBD
    """
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        chrome_options.add_argument("window-size=1920x1080")
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.close()


class TestHome(TestPyOrgBase):
    """
    TBD
    """
    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    def test_TC001_py3_python_news_button(self):
        self.home.hover_to(CommonPageLocators.NEWS)
        self.home.assert_elem_text(CommonPageLocators.PYTHON_NEWS_BUTTON, "Python News")
        self.home.click(CommonPageLocators.PYTHON_NEWS_BUTTON)
        self.assertEqual(self.driver.current_url, "https://www.python.org/blogs/")


class TestBlog(TestPyOrgBase):
    """
    TBD
    """
    def setUp(self):
        super().setUp()
        self.blog = BlogPage(self.driver)

    def test_TC002_verify_url(self):
        self.blog.click(BlogPageLocators.PY380RC1)
        self.assertEqual(self.driver.current_url, "https://pythoninsider.blogspot.com/2019/10/"
                                                  "python-380rc1-is-now-available.html?utm_source="
                                                  "feedburner&utm_medium=feed&utm_campaign=Feed%3A+PythonInsider+"
                                                  "%28Python+Insider%29")

    def test_TC003_verify_PY380RC1_name(self):
        self.blog.click(BlogPageLocators.PY380RC1)
        self.blog.navigate_browser_back()
        self.blog.assert_elem_text(BlogPageLocators.PY380RC1, "Python 3.8.0rc1 is now available")


if __name__ == '__main__':
    unittest.main()
