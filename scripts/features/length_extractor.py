import re
from scripts.features.feature_extractor import FeatureExtractor
from bs4 import BeautifulSoup


class TitleLengthExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        return len(post.title)


class SectionCountExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        count = 0
        for ln in lines:
            if ln.startswith("#"):
                count += 1
        return count


class SentenceInfo():

    def __init__(self, body):
        self.body = body

        self.sentence_count = 0
        self.all_sentence_length = 0
        self.max_sentence_length = 0
        self.min_sentence_length = 0
        self.all_char_count = 0
        self.kanji_char_count = 0
        self.hiragana_char_count = 0
        self.katakana_char_count = 0
        self.alphabet_char_count = 0
        self.number_char_count = 0

        self.regex_kanji = '[一-龥]'
        self.regex_hiragana = '[ぁ-ん]'
        self.regex_katakana = '[ァ-ン]'
        self.regex_alphabet = '[a-xA-Z]'
        self.regex_number = '[0-9]'

    def analyse(self):
        lines = self.body.split("\n")

        kanji_pattern = re.compile(self.regex_kanji)
        hiragana_pattern = re.compile(self.regex_hiragana)
        katakana_pattern = re.compile(self.regex_katakana)
        alphabet_pattern = re.compile(self.regex_alphabet)
        number_pattern = re.compile(self.regex_number)

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                self.sentence_count += 1
                self.all_sentence_length += len(ln)

                if self.max_sentence_length < len(ln):
                    self.max_sentence_length = len(ln)

                if self.min_sentence_length > len(ln) or self.min_sentence_length == 0:
                    self.min_sentence_length = len(ln)

                for char in ln:
                    if re.search(kanji_pattern, char) is not None:
                        self.kanji_char_count += 1
                    if re.search(hiragana_pattern, char) is not None:
                        self.hiragana_char_count += 1
                    if re.search(katakana_pattern, char) is not None:
                        self.katakana_char_count += 1
                    if re.search(alphabet_pattern, char) is not None:
                        self.alphabet_char_count += 1
                    if re.search(number_pattern, char) is not None:
                        self.number_char_count += 1

                    self.all_char_count += 1


class SentenceMeanLengthExtractor(FeatureExtractor):

    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.all_sentence_length / self.SentenceInfo.sentence_count


class SentenceMaxLengthExtractor(FeatureExtractor):

    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.max_sentence_length


class SentenceMinLengthExtractor(FeatureExtractor):

    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.min_sentence_length


class KanjiRatioExtractor(FeatureExtractor):

    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.kanji_char_count / self.SentenceInfo.all_char_count


class HiraganaRatioExtractor(FeatureExtractor):

    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.hiragana_char_count / self.SentenceInfo.all_char_count


class KatakanaRatioExtractor(FeatureExtractor):
    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.katakana_char_count / self.SentenceInfo.all_char_count


class AlphabetRatioExtractor(FeatureExtractor):
    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.alphabet_char_count / self.SentenceInfo.all_char_count


class NumberRatioExtractor(FeatureExtractor):
    def __init__(self, SentenceInfo):
        self.SentenceInfo = SentenceInfo

    def extract(self, post, extracted=None):
        return self.SentenceInfo.number_char_count / self.SentenceInfo.all_char_count


class Header1MeanLengthExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        soup = BeautifulSoup(post.rendered_body, "html5lib")
        header1s = soup.find_all('h1')
        sentence_count = 0
        count_sentence_length = 0
        for ln in header1s:
            count_sentence_length += int(len(ln.text))
            sentence_count += 1

        if count_sentence_length != 0:
            header_mean_length = count_sentence_length / sentence_count
        else:
            header_mean_length = 0

        return header_mean_length


class Header2MeanLengthExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        soup = BeautifulSoup(post.rendered_body, "html5lib")
        header1s = soup.find_all('h2')
        sentence_count = 0
        count_sentence_length = 0
        for ln in header1s:
            count_sentence_length += int(len(ln.text))
            sentence_count += 1

        if count_sentence_length != 0:
            header_mean_length = count_sentence_length / sentence_count
        else:
            header_mean_length = 0

        return header_mean_length
