import re
from bs4 import BeautifulSoup
from scripts.features.feature_extractor import FeatureExtractor
from scripts.data.preprocessing import cleaning


class RenderedBodyPreprocessor():

    def clean_rendered_body(self, rendered_body):
        cleaned_rendered_body = cleaning(rendered_body)
        return cleaned_rendered_body


class CharacterRatio():
    def __init__(self, regex_text, text):
        self.regex = regex_text
        self.text = text

    def character_ratio(self):
        pattern = re.compile(self.regex)
        count = len(re.findall(pattern, self.text))
        ratio = count / len(self.text)
        return ratio


class KanjiRatioExtractor(FeatureExtractor):
    def __init__(self, cleaned_rendered_body):
        self.regex_text = '[一-龥]'
        self.character_ratio = CharacterRatio(self.regex_text, cleaned_rendered_body)

    def extract(self, post, extracted=None):
        ratio = self.character_ratio.character_ratio()
        return ratio


class HiraganaRatioExtractor(FeatureExtractor):
    def __init__(self, cleaned_rendered_body):
        self.regex_text = '[ぁ-ん]'
        self.character_ratio = CharacterRatio(self.regex_text, cleaned_rendered_body)

    def extract(self, post, extracted=None):
        ratio = self.character_ratio.character_ratio()
        return ratio


class KatakanaRatioExtractor(FeatureExtractor):
    def __init__(self, cleaned_rendered_body):
        self.regex_text = '[ァ-ン]'
        self.character_ratio = CharacterRatio(self.regex_text, cleaned_rendered_body)

    def extract(self, post, extracted=None):
        ratio = self.character_ratio.character_ratio()
        return ratio


class AlphabetRatioExtractor(FeatureExtractor):
    def __init__(self, cleaned_rendered_body):
        self.regex_text = '[a-xA-Z]'
        self.character_ratio = CharacterRatio(self.regex_text, cleaned_rendered_body)

    def extract(self, post, extracted=None):
        ratio = self.character_ratio.character_ratio()
        return ratio


class NumberRatioExtractor(FeatureExtractor):
    def __init__(self, cleaned_rendered_body):
        self.regex_text = '[0-9]'
        self.character_ratio = CharacterRatio(self.regex_text, cleaned_rendered_body)

    def extract(self, post, extracted=None):
        ratio = self.character_ratio.character_ratio()
        return ratio


class PunctuationRatioExtractor(FeatureExtractor):
    def __init__(self, cleaned_rendered_body):
        self.regex_text = '[、。]'
        self.character_ratio = CharacterRatio(self.regex_text, cleaned_rendered_body)

    def extract(self, post, extracted=None):
        ratio = self.character_ratio.character_ratio()
        return ratio
