from selene import be, by, browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    s(by.link_text('eroshenkoam/allure-example')).click()

    s("#issues-tab").click()

    s(by.partial_text('#65')).should(be.visible)
