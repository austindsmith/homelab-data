import re
import os
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import Playwright, sync_playwright, expect

load_dotenv(override=False)


## Variables

WATER_URL = os.environ["WATER_URL"]
WATER_EMAIL = os.environ["WATER_EMAIL"]
WATER_PASSWORD = os.environ["WATER_PASSWORD"]
WATER_FILE_NAME = os.environ["WATER_FILE_NAME"]
WATER_PAGE_NAME = os.environ["WATER_PAGE_NAME"]

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(WATER_URL)
    page.get_by_role("link", name="MY ACCOUNT").click()
    page.locator("[data-test=\"sign-in-email-input\"]").click()
    page.locator("[data-test=\"sign-in-email-input\"]").fill(WATER_EMAIL)
    page.locator("[data-test=\"sign-in-password-input\"]").click()
    page.locator("[data-test=\"sign-in-password-input\"]").fill(WATER_PASSWORD)
    page.get_by_role("button", name="Sign In", exact=True).click()
    page.get_by_role("button", name="VIEW/PAY BILL").click()
    page.get_by_role("link", name="History").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Export").click()
    download = download_info.value
    path = download.path()              # temp path managed by Playwright
    download.save_as(WATER_FILE_NAME)
    page.get_by_role("button", name=WATER_PAGE_NAME).click()
    page.get_by_role("link", name="Log Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

