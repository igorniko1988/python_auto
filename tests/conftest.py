import pytest
import os
from selene.support.shared import browser
from selene.core import command
from todomvc_tests.models.pages.application import App
from todomvc_tests import options

@pytest.fixture
def app():
    yield App


@pytest.fixture(scope='function', autouse=True)
def browser_managment(app):
    browser.config.driver_name = options.get('browser', 'safari')
    yield
    if options.get('close_browser','true') == 'true':
        browser.clear_local_storage()