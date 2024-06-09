from playwright.sync_api import sync_playwright
from time import time, sleep

start = time()
with sync_playwright() as p:
    browser = p.webkit.launch(headless=True)
    context = browser.new_context(record_video_dir="videos/", record_video_size={"width": 640, "height": 480})
    page = context.new_page()
    page.goto('https://www.twitch.tv/thebausffs')
    sleep(40)
    browser.close()
print(time() - start, ' - Время выполнения')