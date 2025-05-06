from playwright.sync_api import sync_playwright

from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for character in 'user@gmail.com':
        page.keyboard.press(character, delay=300)

    page.keyboard.press("ControlOrMeta+A")