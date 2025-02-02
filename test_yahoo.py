import os
os.environ["PWDEBUG"] = "1" #the test is opened in a visible window so you can see what's happening

import asyncio
from playwright.async_api import async_playwright, Playwright, Page, expect

async def main():
    async with async_playwright() as playwright:
    
        #sets up the tab
        chromium = playwright.chromium
        browser = await chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-GB&.intl=gb&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%2F")
        #sign in  
        
        await page.get_by_placeholder(" ").click() #only part from the inspect element that could be used to locate
        await page.keyboard.type("testplaywright@myyahoo.com")
        await page.keyboard.press("Enter")
        
        
        await expect(page.get_by_text("Enter password")).to_be_visible()
        await page.get_by_placeholder(" ").click()
        await page.keyboard.type("playwrightpassword!")
        await page.keyboard.press("Enter")
        #select the second unread email matching search term
        await expect(page.get_by_text("Unread")).to_be_visible()
        await page.get_by_text("Unread").click()
        await page.get_by_placeholder("Search in unread..").fill("test")
        await page.keyboard.press("Enter")
        await page.get_by_role("gridcell", name="Select message").nth(1).click() #selects second unread email
        await page.keyboard.press("Enter")
        await page.keyboard.type("Here so the debugger doesn't close before showing that the email is opened")
        








if __name__ == "__main__":  
    asyncio.run(main())