import allure
from allure_commons.types import Severity
from selene import be, by, browser
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'belov d.k.')
@allure.feature('Поиск')
@allure.story('Поиск определенного репо и задачи в нем')
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.open('/')

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()
    s(by.link_text('eroshenkoam/allure-example')).click()

    s("#issues-tab").click()

    s(by.partial_text('#65')).should(be.visible)
