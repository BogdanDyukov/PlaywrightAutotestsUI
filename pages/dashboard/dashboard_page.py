import allure
from playwright.sync_api import Page, expect

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Интегрируем компоненты
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)

        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")

    @allure.step("Check visible charts")
    def check_visible_charts(self):
        self.scores_chart_view.check_visible('Scores')
        self.courses_chart_view.check_visible('Courses')
        self.students_chart_view.check_visible('Students')
        self.activities_chart_view.check_visible('Activities')
