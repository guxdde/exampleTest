# -*-  coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # selenium等待3秒钟，等待加载

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

        # 他注意到网页的标题和头部都包含To-Do这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请他输入一个代办事项
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # 他在一个文本矿中输入了“Buy peacock feathers”(购买孔雀羽毛)
        # 伊迪斯等爱好时使用假蝇做鱼饵钓鱼
        input_box.send_keys('Buy peacock feathers')

        # 他按回车键后，页面更新了
        # 代办事项表格中显示了“1：Buy peacock feathers”
        input_box.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1:Buy peacock feathers')
        time.sleep(10)
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        # any(row.text == '1:Buy peacock feathers' for row in rows),
        # "New to-do item did not appear in table--its text was:\n%s" % (table.text,))
        # self.assertIn('1:Buy peacock feathers', [row.text for row in rows])

        # 他输入了“Use peacock feathers to make a fly”（使用孔雀毛做假蝇）
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2:Use peacock feathers to make a fly')
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1:Buy peacock feathers', [row.text for row in rows])
        # self.assertIn(
        #     '2:Use peacock feathers to make a fly', [row.text for row in rows])

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
