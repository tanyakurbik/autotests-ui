from playwright.sync_api import sync_playwright, expect

from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.fill("username")

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title_name = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title_name).to_be_visible()
    expect(courses_title_name).to_have_text("Courses")

    folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(folder_icon).to_be_visible()

    courses_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title_text).to_be_visible()
    expect(courses_title_text).to_have_text("There is no results")

    courses_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description_text).to_be_visible()
    expect(courses_description_text).to_have_text("Results from the load test pipeline will be displayed here")

