from playwright.sync_api import sync_playwright
import re
from playwright.sync_api import expect
import time



def test_my_gui():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox]:
            browser = browser_type.launch(headless=False)
            page = browser.new_page()
            page.goto("http://delayounce.herokuapp.com/")
            page.click('li#NextButton a.page-link')
            page.click('li#about\\ us\\ Button a.nav-link')




test_my_gui()
