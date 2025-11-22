import allure
from selene import browser, have
from pages.practice_form_page import PracticeFormPage


@allure.title("Заполнение формы Practice Form (Allure screenshot/video)")
def test_practice_form():
    form = PracticeFormPage()

    with allure.step("Открыть форму"):
        form.open()

    with allure.step("Заполнить форму"):
        form.fill()

    with allure.step("Отправить форму"):
        form.submit()

    with allure.step("Проверить, что форма успешно отправлена"):
        browser.element(".modal-header").should(have.text("Thanks for submitting the form"))
