# -*-  coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time


class NewVisitorTest(LiveServerTestCase):

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
        self.browser.get(self.live_server_url)

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

        # 他按回车键后，被带到了一个新URL
        # 代办事项表格中显示了“1：Buy peacock feathers”
        input_box.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        # Python 2 – then use assertRegexpMatches instead of assertRegex
        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        time.sleep(10)

        # 他输入了“Use peacock feathers to make a fly”（使用孔雀毛做假蝇）
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2:Use peacock feathers to make a fly')

        # 现在一个叫弗朗西斯等新用户访问了网站
        # 我们使用一个新浏览器会话
        # 确保伊迪斯的信息不会从cookie中泄露出来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 弗朗西斯访问首页
        # 页面中看不到伊迪斯的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        # 弗朗西斯输入一个新代办事项，新建一个清单
        # 他不像伊迪斯那样兴趣盎然
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        # 弗朗西斯获得了他的唯一URL
        francis_list_url = self.browser.current_url
        # Python 2 – then use assertRegexpMatches instead of assertRegex
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        # 这个页面还是没有伊迪斯的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        # 两个人都很满意，去睡觉了

        self.fail('Finish the test!')
