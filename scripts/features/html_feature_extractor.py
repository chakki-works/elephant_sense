import re
from scripts.features.feature_extractor import FeatureExtractor
from bs4 import BeautifulSoup


class HeaderCountExtractor(FeatureExtractor):

    def __init__(self, html=None):
        self.cache = html

    def extract(self, post, extracted=None):
        html = self.get_html(post)
        headers = html.find_all("h1")
        return len(headers)
    
    def get_html(self, post):
        if self.cache:
            return self.cache
        else:
            return BeautifulSoup(post.rendered_body, "html.parser")


class HeaderCountExtractor(FeatureExtractor):

    def __init__(self, html=None):
        self.cache = html

    def extract(self, post, extracted=None):
        html = self.get_html(post)
        headers = html.find_all("h1")
        return len(headers)
    
    def get_html(self, post):
        if self.cache:
            return self.cache
        else:
            return BeautifulSoup(post.rendered_body, "html.parser")
