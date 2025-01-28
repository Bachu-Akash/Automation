import pytest
from selenium import webdriver
import time
from Library.common_functions import CommonFunctions

class TestEcommercePracticePage:

    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.common=CommonFunctions(self.driver)

    def testcase_1_check_options_display(self):
        self.common.open_url(self.common.locators["base_url"])
        self.common.click_element("practice_button")

        ecommerce_option_display=self.common.is_displayed("ecommerce_option")
        element_option_display=self.common.is_displayed("element_option")

        assert ecommerce_option_display,"eCommerce option is not displayed"
        assert element_option_display,"element option is not displayed"
        print("Test Case Passed: Both options are displayed correctly.")

    def testcase_2_redirect_to_ecommerce_practice(self):
        self.common.open_url(self.common.locators["base_url"])
        self.common.click_element("practice_button")
        self.common.click_element("ecommerce_option")

        original_window = self.driver.current_window_handle
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
        assert self.common.current_url()==self.common.locators["e_commerce_url"],"Redirected URL is incorrect"

    def testcase_3_ecom_page_load(self):
        self.common.open_url(self.common.locators["e_commerce_url"])
        ecom_page=self.common.is_displayed("ecom_body")
        assert ecom_page, "eCommerce page elements were not displayed"

    def testcase_4_ecommerce_login(self):
        self.common.open_url(self.common.locators["e_commerce_login_url"])
        time.sleep(2)
        self.common.send_keys("email_box","thecognitivecoders@gmail.com")
        time.sleep(2)
        self.common.send_keys("password_box","Cognitive@123")
        self.common.click_element("login_button")
        self.common.wait_for_url_change(self.common.locators["ecom_login_redirect_url"])
        assert self.driver.current_url==self.common.locators["ecom_login_redirect_url"],"Redirected URL is incorrect"

    def testcase_5_sort_by_price_not_clickable(self):
        self.common.open_url(self.common.locators["e_commerce_url"])
        self.driver.implicitly_wait(3)
        self.common.click_element("ecom_shop_button")
        assert self.common.is_not_clickable("sort_by_price_button")

    def testcase_9_verify_search_box_display(self):
        self.common.open_url(self.common.locators["e_commerce_url"])
        #time.sleep(3)
        self.common.click_element("search_icon")
        is_search_box_displayed = self.common.is_displayed("search_box")
        assert is_search_box_displayed,"Search box is not displayed on the eCommerce practice page"

    def testcase_10_verify_checkout_process(self):
        self.common.open_url(self.common.locators["e_commerce_url"])
        time.sleep(2)
        self.common.click_element("ecom_bag_button")
        self.common.click_element("ecom_bag_checkout_1")
        time.sleep(2)
        self.common.click_element("ecom_bag_checkout_2")
        assert self.common.is_displayed("order_success_page"),"Checkout order failed"

    def testcase_6_click_product_image_redirect(self):
        self.common.open_url(self.common.locators["e_commerce_url"])
        #time.sleep(2)
        self.common.click_element("shop_t_shirt")
        self.common.wait_for_url_change(self.common.locators["product_detail_page"])
        current_url = self.driver.current_url
        assert current_url==self.common.locators["product_detail_page"],"It is not Redirected to product detail page"

if __name__=="__main__":
    pytest.main()


#python -m pytest Test_Cases/practice_page_test_cases.py -v -s
