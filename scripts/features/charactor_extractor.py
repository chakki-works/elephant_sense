import re
from bs4 import BeautifulSoup
from scripts.features.feature_extractor import FeatureExtractor
from scripts.data.cleaning import clean_code


def clean_html_tags(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    if soup.find("h") is not None:
        soup.find("h").extract()

    cleaned_text = soup.get_text()
    cleaned_text = ''.join(cleaned_text.splitlines())
    return cleaned_text


def clean_code(html_text):
    """Qiitaのコードを取り除きます
    :param html_text:
    :return:
    """
    soup = BeautifulSoup(html_text, 'html.parser')
    [x.extract() for x in soup.findAll(class_="code-frame")]
    [x.extract() for x in soup.findAll("code")]
    cleaned_text = soup.get_text()
    cleaned_text = ''.join(cleaned_text.splitlines())
    return cleaned_text


def cleaning(text):
    replaced_text = clean_code(html_text=text)  # remove source code
    replaced_text = clean_html_tags(html_text=replaced_text)  # remove html tag
    replaced_text = re.sub(r'\$.*?\$+', '', replaced_text)  # remove math equation
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # remove @mention
    replaced_text = re.sub(r'https?:\/\/.*?([\r\n ]|$)', '', replaced_text)  # remove URL
    replaced_text = re.sub(r'　', '', replaced_text)  # remove zenkaku space
    return replaced_text


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
        ratio = 0 if len(self.text) == 0 else count / len(self.text)
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
        self.regex_text = '[、]'
        self.character_ratio = CharacterRatio(self.regex_text, cleaned_rendered_body)

    def extract(self, post, extracted=None):
        ratio = self.character_ratio.character_ratio()
        return ratio
