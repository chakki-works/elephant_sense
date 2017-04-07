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


class SentenceMeanLengthExtractor(FeatureExtractor):
    def __init__(self, text):
        self.text = text

    def extract(self, post, extracted=None):
        lines = self.text.split("。")
        count = 0
        all_sentence_count = 0

        for ln in lines:
            all_sentence_count += len(ln)
            count += 1
        return all_sentence_count / count


class SentenceMaxLengthExtractor(FeatureExtractor):
    def __init__(self, text):
        self.text = text

    def extract(self, post, extracted=None):
        lines = self.text.split("。")
        count = 0
        max_length = 0

        for ln in lines:
            count += 1
            if len(ln) > max_length:
                max_length = len(ln)

        return max_length / count


class SentenceMinLengthExtractor(FeatureExtractor):
    def __init__(self, text):
        self.text = text

    def extract(self, post, extracted=None):
        lines = self.text.split("。")
        count = 0
        min_length = 0

        for ln in lines:
            count += 1
            if len(ln) < min_length or min_length == 0:
                min_length = len(ln)

        return min_length / count


class Header1MeanLengthExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        soup = BeautifulSoup(post.rendered_body, "html.parser")
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
        soup = BeautifulSoup(post.rendered_body, "html.parser")
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
