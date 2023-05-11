from selene.support.shared import browser as shared_browser
from selene import by, have, be


class TodoMvc:
    def __init__(self, browser = shared_browser):
        self.browser = browser

    def open(self, url):
        self.browser.open('https://todomvc.com/examples/emberjs/')
        return self


    def add_todo(self, *todos):
        for todo in todos:
            self.browser.element('#new-todo').type(todo).press_enter()
        return self

    def todo_should_have(self, *text):
        self.browser.all('#todo-list li').should(have.exact_texts(*text))
