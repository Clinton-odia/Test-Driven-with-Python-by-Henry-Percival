# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# # ✅ Updated path
# service = Service(
#     executable_path="C:/Users/USER/Downloads/chromedriver-win64/chromedriver.exe"
# )
# driver = webdriver.Chrome(service=service)

# driver.get("https://www.google.com")
# print("Page title is:", driver.title)

# time.sleep(3)
# driver.quit()

# from selenium import webdriver

# browser = webdriver.Chrome()

# browser.get("http://localhost:8000")

# assert "Congratulations" in browser.title
# print("ok")


"""Acceptance test for the todo app"""

# from selenium import webdriver

# browser = webdriver.Chrome()
# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
# browser.get("http://localhost:8000")
# She notices the page title and header mention to-do lists
# assert "To-Do" in browser.title, f"Browser title error"
# She is invited to enter a to-do item straight away
# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)
# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list
# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly" (Edith is very methodical)
# The page updates again, and now shows both items on her l

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.
# She visits that URL - her to-do list is still there.
# Satisfied, she goes back to sleep
# browser.quit()

# import unittest
# from selenium import webdriver


# class NewVisitorTest(unittest.TestCase):
#     """Test for new web visitor"""

#     def setUp(self):
#         self.browser = webdriver.Chrome()

#     def tearDown(self):
#         self.browser.quit()

#     def test_can_start_todo_list(self):
#         """Test if todo in browser"""
#         self.browser.get("http://localhost:8000")
#         self.assertIn("Todo", self.browser.title)

#         self.fail("finish test")

# if __name__ == "__main__":
#     unittest.main()

# extended version

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists:
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)  # Wait for page to update

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows),
            "New to-do item not found in table",
        )

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
