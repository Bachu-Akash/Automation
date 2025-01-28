import pytest
from selenium import webdriver
from Library.common_functions import CommonFunctions
import time

class TestElementPracticePage:

    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.common=CommonFunctions(self.driver)

    def testcase_11_redirect_to_element_practice(self):
        self.common.open_url(self.common.locators["base_url"])
        self.common.click_element("practice_button")
        self.common.click_element("element_option")
        self.driver.implicitly_wait(3)

        original_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
        assert self.common.current_url()==self.common.locators["element_url"],"Redirected URL is incorrect"

    def testcase_12_element_page_load(self):
        element_page=self.common.is_displayed("element_body")
        assert element_page, "Element page elements were not displayed"

    def testcase_13_test_checkboxes(self):
        self.common.click_element("check_box_1")
        self.common.click_element("check_box_2")
        self.common.click_element("check_box_3")

        self.driver.implicitly_wait(3)

        cb1=self.common.is_displayed("check_box_1")
        cb2=self.common.is_displayed("check_box_2")
        cb3=self.common.is_displayed("check_box_3")

        assert cb1 and cb2 and cb3, "Checkboxes were not selected"

        self.common.click_element("check_box_1")
        self.common.click_element("check_box_2")
        self.common.click_element("check_box_3")

        self.driver.implicitly_wait(3)

        cb1=self.common.is_displayed("check_box_1")
        cb2=self.common.is_displayed("check_box_2")
        cb3=self.common.is_displayed("check_box_3")

        assert cb1 and cb2 and cb3, "Checkboxes were selected"

    def testcase_14_switch_to_alert(self, name="Akash"):
        self.driver.implicitly_wait(4)
        self.common.send_keys("switch_to_alert_name_box", name)
        self.common.click_element("alert_button")
        self.common.handle_alert(action="accept", name=name)

    def testcase_15_switch_to_confirm(self):
        #accept
        self.common.click_element("confirm_button")
        self.common.handle_confirm(action="accept")
        #dismiss
        self.common.click_element("confirm_button")
        self.common.handle_confirm(action="dismiss")

    def testcase_16_mouse_hover_display_options(self):
        self.common.hover_element("hover_element")
        option1_displayed = self.common.is_displayed("hover_option_1")
        option2_displayed = self.common.is_displayed("hover_option_2")

        assert option1_displayed, "Additional option 1 is not displayed"
        assert option2_displayed, "Additional option 2 is not displayed"


    def testcase_18_toggle_textbox_visibility(self):
        is_displayed_initially = self.common.is_displayed("hide/show_textbox")

        assert is_displayed_initially, "Text box should be displayed initially"

        self.common.click_element("hide_button")
        is_displayed_after_hide = self.common.is_displayed("hide/show_textbox")

        assert not is_displayed_after_hide, "Text box should be hidden after clicking hide button"

        self.common.click_element("show_button")
        is_displayed_after_show = self.common.is_displayed("hide/show_textbox")

        assert is_displayed_after_show, "Text box should be displayed after clicking show button"

    def testcase_19_retrieve_table_data(self):
        self.driver.implicitly_wait(3)
        row_index = 2
        column_index = 1
        table_data = self.common.retrieve_table_data("web_table", row_index, column_index)

        assert table_data is not None, "No data retrieved from the specified table cell."
        print(f"Data from Row {row_index}, Column {column_index}: {table_data}")

if __name__=="__main__":
    pytest.main()






