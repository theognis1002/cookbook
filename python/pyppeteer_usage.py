import asyncio

from pyppeteer import launch
from pyppeteer_stealth import stealth


async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()

    await stealth(page)  # <-- Here

    await page.goto("https://bot.sannysoft.com/")
    await page.screenshot({"path": "example.png"})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
