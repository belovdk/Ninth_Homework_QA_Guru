import allure
from selene import be, by, browser
from selene.support.shared.jquery_style import s


def open_main_page():
    browser.open('https://github.com')


@allure.step('В поисковую строку вбиваем название репозитория {repo}')
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем вкладку Issues')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('Провереям наличие задачи под номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#65')
