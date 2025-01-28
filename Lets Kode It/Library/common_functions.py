from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CommonFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "base_url": "https://www.letskodeit.com/",
            "e_commerce_url": "https://ecommercepractice.letskodeit.com/",
            "e_commerce_login_url": "https://ecommercepractice.letskodeit.com/login/",
            "element_url": "https://www.letskodeit.com/practice",
            "practice_button": "//div[@class='dropdown']/a",
            "ecommerce_option": "//a[normalize-space()='eCommerce Practice'][1]",
            "element_option": "//a[normalize-space()='Element Practice'][1]",
            "login_click": "//*[name()='svg'][5]",
            "email_box": "//input[@id='email']",
            "password_box": "//input[@id='password']",
            "login_button": "//button[normalize-space()='LOG IN']",
            "ecom_login_redirect_url": "https://ecommercepractice.letskodeit.com/account/orders/",
            "ecom_body": "(//body)[1]",
            "ecom_bag_button": "//button[@aria-label='Cart']",
            "ecom_bag_checkout_1": "//button[normalize-space()='checkout']",
            "ecom_bag_checkout_2": "//button[normalize-space()='checkout']",
            "order_success_page": "//h1[normalize-space()='Thank You!'][1]",
            "expected_order_success_page_text": "Thank You!",
            "sort_by_price_button": "//span[normalize-space()='Sort by']",
            "ecom_shop_button": "//a[@class='Header-module--navLink--2a5b8 '][normalize-space()='Shop']",
            "shop_t_shirt": "//img[@alt='classic t-shirt 1'][1]",
            "product_detail_page": "https://ecommercepractice.letskodeit.com/product/sample",
            "search_icon": "//button[@aria-label='Search']//*[name()='svg']",
            "search_box": "//input[@id='searchInput'][1]",
            "element_body": "//body",
            "check_box_1": "//input[@type='checkbox' and contains(@id,'bmwcheck')]",
            "check_box_2": "//input[@type='checkbox' and contains(@id,'benzcheck')]",
            "check_box_3": "//input[@type='checkbox' and contains(@id,'hondacheck')]",
            "switch_to_alert_name_box": "//input[@id='name']",
            "alert_button": "//input[@id='alertbtn']",
            "confirm_button": "//input[@id='confirmbtn']",
            "expected_confirm_text": "Are you sure you want to confirm?",
            "hover_element": "//button[@id='mousehover']",
            "hover_option_1": "//a[normalize-space()='Top']",
            "hover_option_2": "//a[normalize-space()='Reload'][1]",
            "hide/show_textbox": "//input[@name='show-hide']",
            "hide_button": "//input[@id='hide-textbox']",
            "show_button": "//input[@id='show-textbox']",
            "web_table": "//table[@id='product']",
            "youtube_button": "//a[@class='fab fa-youtube dynamic-link-icon'][1]",
            "expected_youtube_url": "https://www.youtube.com/c/LetsKodeItOfficial",
            "iframe_id": "//iframe[@id='courses-iframe']",
            "iframe_textbox": "//iframe[@id='courses-iframe']",
            "iframe_search_button": "//*[@id='search']/div/button"
        }

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, xpath, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def wait_for_url_change(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    def is_displayed(self, locator_key):
        element_xpath = self.locators[locator_key]
        element = self.driver.find_element(By.XPATH, element_xpath)
        return element.is_displayed()

    def is_selected(self, locator_key):
        element_xpath = self.locators[locator_key]
        element = self.driver.find_element(By.XPATH, element_xpath)
        return element.is_selected()

    def wait_for_element_clickable(self, locator_key, timeout=15):
        element_xpath = self.locators[locator_key]
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, element_xpath))
        )

    def is_not_clickable(self, locator_key, timeout=10):
        element_xpath = self.locators[locator_key]
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, element_xpath))
            )
            return True
        except:
            return False

    def handle_alert(self, action="accept", name=None, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        if name:
            expected_text = f"Hello {name}, share this practice page and share your knowledge"
            alert_text = alert.text
            assert alert_text == expected_text, "Unexpected alert"
        if action == "accept":
            alert.accept()

    def handle_confirm(self, action="accept", timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        confirm_box = self.driver.switch_to.alert
        confirm_text = confirm_box.text
        expected_text = "Hello , Are you sure you want to confirm?"
        assert confirm_text == expected_text, f"Unexpected confirm box text: {confirm_text}"
        if action == "accept":
            confirm_box.accept()
        elif action == "dismiss":
            confirm_box.dismiss()

    def hover_element(self, locator_key, timeout=10):
        element_xpath = self.locators[locator_key]
        element = self.wait_for_element(element_xpath)
        ActionChains(self.driver).move_to_element(element).perform()

    def retrieve_table_data(self, locator_key, row_index, column_index):
        table_xpath = self.locators[locator_key]
        table = self.wait_for_element(table_xpath)
        rows = table.find_elements(By.TAG_NAME, "tr")

        if row_index < len(rows):
            cols = rows[row_index].find_elements(By.TAG_NAME, "td")
            if column_index < len(cols):
                return cols[column_index].text

        return None

    def send_keys(self, locator_key, input_data, timeout=10):
        element = self.wait_for_element_clickable(locator_key, timeout)
        element.send_keys(input_data)

    def click_element(self, locator_key, timeout=15):
        element = self.wait_for_element_clickable(locator_key, timeout)
        element.click()

    def current_url(self):
        return self.driver.current_url

    def browser_title(self):
        self.driver.title()

    def close_browser(self):
        self.driver.close()
