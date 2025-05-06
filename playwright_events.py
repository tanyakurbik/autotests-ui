from playwright.sync_api import sync_playwright, Request, Response

from config import settings


def log_request(request: Request):
    print(f"Request: {request.url}")

def log_response(response: Response):
    print(f"Response: {response.url}")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=settings.headless)
    page = browser.new_page()

    # Добавляем обработчики событий
    page.on("request", log_request)  # Запрос отправлен
    page.on("response", log_response)  # Ответ получен

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
