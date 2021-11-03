
__appname__ = "pyft"
__version__ = "0.1"

from modules.models.crib import Crib
from modules.models.baby_carriage import BabyCarriage
from modules.models.config import FetcherConfig

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import os
import warnings

from urllib.parse import urljoin

import timestring
import json
import time

import psycopg2 as sql
import urllib.request
import pytz


class Fetcher(object):
    def __init__(self, config):
        self.config = config

        self.conn = sql.connect(dbname='finan', user='postgres',
                                password='postgres', host='database')
        self.cursor = self.conn.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS {} (name text, price real);".
                            format(
                                self.config.site
                            ))
        self.conn.commit()

    def get_endpoint_path(self, endpoint):
        return urljoin(self.config.base_url, endpoint)

    def scroll_(self, counter):
        self.driver.execute_script("""
                sub_window = document.querySelector('{0}');
                sub_window.scrollTo(0, {1}*sub_window.scrollHeight);""".format(self.config.window_selector, counter))
        time.sleep(self.config.SCROLL_PAUSE_TIME)

    def get_config_for_driver_(self):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        op.add_argument('--no-sandbox')
        op.add_argument('--disable-dev-shm-usage')
        return op

    def get_stream(self, goods_type):
        # Configure driver
        op = self.get_config_for_driver_()
        self.driver = webdriver.Chrome(self.config.chromedriver, options=op)

        page_number = self.config.first_page
        page_is_not_empty = True

        while(page_is_not_empty):
            # Initialize
            goods = []
            counter = 0
            content_size = 0

            endpoint = self.get_endpoint_path(
                "{}/{}{}".format(goods_type, self.config.page_format, page_number))

            self.driver.get(endpoint)
            print("Endpoint: ", endpoint)

            # Get goods
            content_list = self.driver.find_elements_by_css_selector(
                self.config.goods_selector)

            while len(content_list) > content_size:
                self.scroll_(counter)
                counter += 1
                content_list = self.driver.find_elements_by_css_selector(
                    self.config.goods_selector)
                content_size = len(content_list)

                print("Counter: ", counter, ", content length: ", content_size)

            print("Found {} goods without filters".format(content_size))

            # Parse each good and insert to database
            for content in content_list:
                try:
                    name = content.find_element_by_css_selector(
                        self.config.good_name_selector).text

                    for selector in self.config.good_price_selectors:
                        try:
                            price = content.find_element_by_css_selector(selector)
                            if price:
                                if self.config.price_is_text:
                                    price = price.text
                                else:
                                    price = price.get_attribute('content')
                                break
                        except:
                            pass

                    obj = BabyCarriage(name, price)
                    dict_obj = obj.get_dict()

                    print("{} \n".format(dict_obj))
                    insert = ('INSERT INTO {} ({}) VALUES ({})').format(
                        self.config.site,
                        ",".join(list(dict_obj.keys())),
                        ",".join(list(dict_obj.values()))
                    )

                    self.cursor.execute(insert)
                except Exception as e:
                    print("Can't parse content: ", str(e))
            self.conn.commit()

            page_number += self.config.step
            page_is_not_empty = bool(content_size)
            
            if self.config.max_pages and self.config.max_pages < page_number:
                break
                
