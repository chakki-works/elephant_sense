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

