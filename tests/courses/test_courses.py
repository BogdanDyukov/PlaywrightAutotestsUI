import allure
import pytest

from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.open(AppRoute.COURSES)
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @pytest.mark.parametrize("title, description, estimated_time, max_score, min_score", [
        ("Playwright", "Playwright", "2 weeks", "100", "10")
    ])
    @allure.title("Create course")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_course(
            self, create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage,
            title: str,
            description: str,
            estimated_time: str,
            max_score: str,
            min_score: str
    ):
        create_course_page.open(AppRoute.CREATE_COURSE)
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible()
        create_course_page.create_course_form.fill(
            title='', description='', estimated_time='', max_score='0', min_score='0'
        )
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title=title, description=description, estimated_time=estimated_time, max_score=max_score, min_score=min_score
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title=title, max_score=max_score, min_score=min_score, estimated_time=estimated_time
        )

    @pytest.mark.parametrize("title, description, estimated_time, max_score, min_score", [
        ("Playwright", "Playwright", "2 weeks", "100", "10")
    ])
    @allure.title("Edit course")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage,
            title: str,
            description: str,
            estimated_time: str,
            max_score: str,
            min_score: str
    ):
        create_course_page.open(AppRoute.CREATE_COURSE)
        create_course_page.create_course_form.fill(
            title=title, description=description, estimated_time=estimated_time, max_score=max_score, min_score=min_score
        )
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0, title=title, max_score=max_score, min_score=min_score, estimated_time=estimated_time
        )
        courses_list_page.course_view.kebab.click_edit(index=0)

        create_course_page.create_course_toolbar_view.check_visible(
            title='Update course', is_create_course_disabled=False
        )
        create_course_page.create_course_form.fill(
            title=title + 'v2',
            description=description + 'v2',
            estimated_time=estimated_time + 'v2',
            max_score=max_score + '0',
            min_score=min_score + '0'
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.course_view.check_visible(
            index=0,
            title=title + 'v2',
            max_score=max_score + '0',
            min_score=min_score + '0',
            estimated_time=estimated_time + 'v2'
        )
