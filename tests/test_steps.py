import allure
from selene import be, by, browser
from selene.support.shared.jquery_style import s


def test_github():
    with allure.step('Открываем страницу https://github.com'):
        browser.open('/')

    with allure.step('В поисковую строку вбиваем название репозитория'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step('Ищем нужный репозиторий'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем вкладку Issues'):
        s("#issues-tab").click()

    with allure.step('Провереям наличие задачи под номером 65'):
        s(by.partial_text('#65')).should(be.visible)



