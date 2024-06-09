import asyncio
from playwright.async_api import async_playwright
from time import time

start = time()

async def play_video(instance_number):
    async with async_playwright() as p:
        engine = p.chromium
        browser = await engine.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.youtube.com/watch?v=dQw4w9WgXcQ', timeout=60000, wait_until='domcontentloaded')
        await page.keyboard.press('k')
        await asyncio.sleep(60)
        await browser.close()

async def main():
    tasks = [play_video(i) for i in range(1, 4)]
    await asyncio.gather(*tasks)

asyncio.run(main())
print(time() - start, ' - Время выполнения')