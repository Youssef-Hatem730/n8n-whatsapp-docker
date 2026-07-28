import asyncio
from playwright.async_api import async_playwright
import time # Import time for delays
import sys
import random
scroll=random.randint(1,3)
search=sys.argv[1]
url = f"https://www.pinterest.com/search/pins/?q={search}&rs=typed"

async def scrape_pinterest_pins():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

      #  print(f"Navigating to {url}")
        await page.goto(url, wait_until='domcontentloaded')

        # Add a small delay to ensure visual rendering after network idle
        await page.wait_for_timeout(3000) # Wait for 3 seconds

        # --- Scroll down to load more content ---
      #  print("Scrolling down to load more content...")
        for _ in range(scroll): # Scroll 5 times (adjust as needed)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000) # Wait for content to load after scroll
      #  print("Finished scrolling.")
        # ----------------------------------------

        try:
          #  print("Waiting for a Pinterest pin element to be visible (max 30 seconds)...")
            pin_selector = 'div[data-test-id="non-story-pin-image"]'

            await page.wait_for_selector(pin_selector, timeout=30000)
           # print("At least one pin element found. Extracting pin information.")

            pin_elements = await page.locator(pin_selector).all()
            #print(f"Found {len(pin_elements)} pins on the page.")

            extracted_pins = []
            for i, pin_element in enumerate(pin_elements):
                if i >= 40: # Extract only first 40 for brevity
                    break
                pin_data = {}
                img_locator = pin_element.locator('img')
                if await img_locator.count() > 0:
                    pin_data['image_src'] = await img_locator.first.get_attribute('src')
                    pin_data['image_alt'] = await img_locator.first.get_attribute('alt')

                
                extracted_pins.append(pin_data["image_src"])
            # Move the return statement outside the loop
            return extracted_pins
        except Exception as e:
            print(f"Error during element extraction: {e}")
            print("Could not find expected dynamic elements or timed out. Check the screenshot and selectors.")

        await browser.close()
      #  print("Browser closed.")
        # If an error occurs or no pins are found, return an empty list
        return []


async def main():
  #  print("Main program started.")
    # Awaiting the coroutine extracts its return value
    result = await scrape_pinterest_pins()
    print(result)

# Entry point to execute the asynchronous program
asyncio.run(main())

