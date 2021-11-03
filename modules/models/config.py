import json
import pytz


class FetcherConfig:
    def __init__(self, base_url, site, goods_selector, good_name_selector, good_price_selectors, window_selector, price_is_text, page_format, max_pages=None, first_page=1, step=1):
        self.chromedriver = "/usr/local/bin/chromedriver"
        self.timezone = pytz.timezone('US/Eastern')
        self.SCROLL_PAUSE_TIME = 0.5

        self.base_url = base_url
        self.site = site

        self.goods_selector = goods_selector
        self.good_name_selector = good_name_selector
        self.good_price_selectors = good_price_selectors

        self.price_is_text = price_is_text
        self.window_selector = window_selector
        self.page_format = page_format
        
        self.first_page = first_page
        self.max_pages = max_pages
        self.step = step
