from selene import browser


class PracticeFormPage:

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        return self

    def fill(self):
        browser.element("#firstName").type("Daria")
        browser.element("#lastName").type("QA")
        browser.element("#userEmail").type("daria@example.com")
        browser.element("//label[text()='Female']").click()
        browser.element("#userNumber").type("8911123456")
        browser.element("#currentAddress").type("Saint-Petersburg")
        return self

    def submit(self):
        browser.element("#submit").click()
        return self
