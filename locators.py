from selenium.webdriver.common.by import By


class CommonPageLocators:
    NEWS = (By.ID, "news")
    PYTHON_NEWS_BUTTON = (By.CSS_SELECTOR, "#news > ul > li.tier-2.element-1 > a")


class BlogPageLocators:
    PY380RC1 = (By.CSS_SELECTOR, "#content > div > section > div > div.most-recent-posts > div > ul > "
                                 "li:nth-child(2) > h3 > a")
