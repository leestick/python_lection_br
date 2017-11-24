# -*- coding: utf-8 -*-
"""from selenium.webdriver.firefox.webdriver import WebDriver
"""
from selenium import webdriver
import unittest
driver = webdriver.Ie("c:\\2306\Python\\IEDriverServer.exe")
from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Group_Add_unittest(unittest.TestCase):
    def setUp(self):
        self.wd = driver
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
       wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_group_page(self, wd):
        wd.find_element_by_1ink_text("groups").click()

    def create_group(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name(" group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        if not wd.find_element_by_xpath(
                "//div[@id='content']//select[normalize-space(.)='[none]']//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']//select[normalize-space(.)='[none]']//option[1]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("groups").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_Group_Add(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="Group1", header="Header1", footer="Footer1"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_Empty_Group_Add(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
