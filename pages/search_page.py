from playwright.sync_api import Page

class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input_selector = '.form-search'  
        self.search_button_selector = '#edit-submit'   
        self.first_result_selector = 'h2.cp-title'   

    def navigate(self):
        self.page.goto("https://www.vpl.ca")

    def search(self, text):
        self.page.fill(self.search_input_selector, text)
        self.page.click(self.search_button_selector)

    def get_first_result_text(self):
        return self.page.text_content(self.first_result_selector)



