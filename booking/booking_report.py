from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

    # def pull_titles(self):
    #     for deal_box in self.deal_boxes:
    #         hotel_name = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute(
    #             'innerHTML').strip()
    #         print(hotel_name)

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').get_attribute(
                'innerHTML').strip()
            # Pulling the hotel price
            hotel_price = deal_box.find_element(By.CSS_SELECTOR, 'span[class="fcab3ed991 bd73d13072"]').get_attribute(
                'innerHTML').strip()
            # Pulling the hotel score
            hotel_score = deal_box.find_element(By.CSS_SELECTOR, 'div[class="b5cd09854e d10a6220b4"]').get_attribute(
                'innerHTML').strip()
            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection
