from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

# ส่วนตั้งค่า Firefox (จำเป็นสำหรับเครื่อง Linux ที่ลงผ่าน Snap)
options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        # แก้ไข 1: ใช้ By.ID แทน find_element_by_id
        table = self.browser.find_element(By.ID, 'id_list_table')
        # แก้ไข 2: ใช้ By.TAG_NAME แทน find_elements_by_tag_name
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        
        # แก้ไข 3: ใช้ By.TAG_NAME
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        # แก้ไข 4: ใช้ By.ID
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1) # รอให้หน้าเว็บโหลด
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly"
        # แก้ไข 5: ใช้ By.ID อีกครั้ง
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()