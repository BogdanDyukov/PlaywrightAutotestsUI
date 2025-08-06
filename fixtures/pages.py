import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from playwright.sync_api import Page


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


# Этот дашборд нужен для теста после успешной регистрации
# Поэтому использует страницу без сохраненного состояния авторизации
@pytest.fixture
def dashboard_page(chromium_page: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page)


# Этот дашборд требует предварительной авторизации
# Чтобы сразу зайти на страницу
@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=chromium_page_with_state)


@pytest.fixture
def courses_list_page(chromium_page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=chromium_page_with_state)


@pytest.fixture
def create_course_page(chromium_page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=chromium_page_with_state)
