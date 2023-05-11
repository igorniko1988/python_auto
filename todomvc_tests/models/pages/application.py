from todomvc_tests.models.pages.todomvc import TodoMvc
from selene.support.shared import browser as shared_browser
from selene import by, have, be


class Application:
    def __init__(self, browser = shared_browser):
        self.todomvc = TodoMvc(browser=browser)


App = Application()