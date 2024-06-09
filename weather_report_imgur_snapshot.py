import asyncio
from os import path
from playwright.async_api import async_playwright
from time import time
import aiofiles


async def imgur_download() -> None:
    async with async_playwright() as p:
        engine = p.chromium
        browser = await engine.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://imgur.com/upload", wait_until="domcontentloaded")
        await page.get_by_text("Choose Photo/Video").click()
        await page.get_by_label("Choose Photo/Video").set_input_files([
            path.join('Biysk-weather.png'),
            path.join('Novosibirsk-weather.png'),
        ])
        await asyncio.sleep(5)
        async with aiofiles.open('imgur_url.txt', 'w') as file:
            await file.write(page.url)
        await asyncio.sleep(5)
        await browser.close()


async def novosibirsk_pogoda() -> None:
    async with async_playwright() as p:
        engine = p.chromium
        browser = await engine.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.gismeteo.ru/", wait_until="domcontentloaded")
        await page.get_by_placeholder("поиск — через пробел можно уточнить страну или регион").click()
        await page.get_by_placeholder("поиск — через пробел можно уточнить страну или регион").fill("Новосибирск")
        await asyncio.sleep(1)
        await page.get_by_placeholder("поиск — через пробел можно уточнить страну или регион").press("Enter")
        await asyncio.sleep(1)
        await page.screenshot(path='Novosibirsk-weather.png', full_page=True)
        await browser.close()


async def biysk_pogoda() -> None:
    async with async_playwright() as p:
        engine = p.chromium
        browser = await engine.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.gismeteo.ru/", wait_until="domcontentloaded")
        await page.get_by_placeholder("поиск — через пробел можно уточнить страну или регион").click()
        await page.get_by_placeholder("поиск — через пробел можно уточнить страну или регион").fill("Бийск")
        await asyncio.sleep(1)
        await page.get_by_placeholder("поиск — через пробел можно уточнить страну или регион").press("Enter")
        await asyncio.sleep(1)
        await page.screenshot(path='Biysk-weather.png', full_page=True)
        await browser.close()


async def main():
    tasks = [novosibirsk_pogoda(), biysk_pogoda()]
    await asyncio.gather(*tasks)
    await imgur_download()


start = time()
asyncio.run(main())
print(time() - start, ' - Время выполнения')