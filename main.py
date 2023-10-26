import os
from dotenv import load_dotenv

load_dotenv()


import time
from playwright.sync_api import Playwright, sync_playwright, expect

target_url: str = "https://jabwi.convergentcare.com/jabwi/goToLogin.action?navStep=#Application/onReady"
username: str = os.getenv("USERNAME")
password: str = os.getenv("PASSWORD")
payment_amount: str = os.getenv("PAYMENT_AMOUNT")

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(target_url)
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)
    time.sleep(5)
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Pay Bill").click()
    print("Logging in..")
    page.locator("#radiofield-1144-displayEl").click()
    page.locator("#textfield-1145-inputEl").click()
    page.locator("#textfield-1145-inputEl").fill(payment_amount)
    print(f"Paying {payment_amount}")
    time.sleep(5)
    page.get_by_label("Payment Date(mm/dd/yyyy)").click()
    page.locator("#csgdatefield-1152-trigger-picker").click()
    page.get_by_title("Next Month (Control+Right)").click()
    page.get_by_text("17", exact=True).click()
    print("Selecting payment date..")
    time.sleep(5)
    page.get_by_role("button", name="Submit Payment").click()
    print("Submitting payment...")
    time.sleep(5)
    page.get_by_role("button", name="Cancel").click()
    print("Canceling payment...")
    time.sleep(5)
    print("Done")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)