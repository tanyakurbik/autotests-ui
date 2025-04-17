import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title_name = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title_name).to_be_visible()
    expect(courses_title_name).to_have_text("Courses")

    folder_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(folder_icon).to_be_visible()

    courses_title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title_text).to_be_visible()
    expect(courses_title_text).to_have_text("There is no results")

    courses_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description_text).to_be_visible()
    expect(courses_description_text).to_have_text("Results from the load test pipeline will be displayed here")
