import re
from scripts.features.feature_extractor import FeatureExtractor
from bs4 import BeautifulSoup


class ItemizationCountExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        soup = BeautifulSoup(post.rendered_body, "html.parser")
        count = len(soup.find_all("ul"))

        return count


class ImageCountExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        soup = BeautifulSoup(post.rendered_body, "html.parser")
        count = len(soup.find_all("img"))

        return count


class FormulaCountExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        count = len(re.findall(r'\$.*?\$+', post.rendered_body))
        return count


class ItemizationRatioExtractor(FeatureExtractor):

    def __init__(self, text):
        self.text = text

    def extract(self, post, extracted=None):
        soup = BeautifulSoup(post.rendered_body, "html.parser")
        target_count = len(soup.find_all("ul"))
        lines_count = len(self.text.split("。"))

        ratio = target_count / lines_count if target_count != 0 else 0
        return ratio


class ImageRatioExtractor(FeatureExtractor):

    def __init__(self, text):
        self.text = text

    def extract(self, post, extracted=None):
        soup = BeautifulSoup(post.rendered_body, "html.parser")
        target_count = len(soup.find_all("img"))
        lines_count = len(self.text.split("。"))

        ratio = target_count / lines_count if target_count != 0 else 0
        return ratio


class FormulaRatioExtractor(FeatureExtractor):

    def __init__(self, text):
        self.text = text

    def extract(self, post, extracted=None):
        target_count = len(re.findall(r'\$.*?\$+', post.rendered_body))
        lines_count = len(self.text.split("。"))

        ratio = target_count / lines_count if target_count != 0 else 0
        return ratio
