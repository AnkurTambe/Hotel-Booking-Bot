from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_value):
        # self.driver.implicitly_wait(15)
        # star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        # star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        #
        # for star_value in star_values:
        #     for star_element in star_child_elements:
        #         if str(star_element.get_attribute('data-filters-item')).strip() == f'class:class={star_value}':
        #             star_element.click()

        rate_checkbox = self.driver.find_element(By.CSS_SELECTOR, f'div[data-filters-item="class:class={star_value}"]')
        rate_checkbox.click()
