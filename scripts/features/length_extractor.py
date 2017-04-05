import re
from scripts.features.feature_extractor import FeatureExtractor


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

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        sentence_count = 0
        all_sentence_length = 0

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                sentence_count += 1
                all_sentence_length += len(ln)
        return all_sentence_length / sentence_count


class SentenceMaxLengthExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        max_sentence_length = 0

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                if max_sentence_length < len(ln):
                    max_sentence_length = len(ln)
        return max_sentence_length


class SentenceMinLengthExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        min_sentence_length = 0

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                if min_sentence_length > len(ln) or min_sentence_length == 0:
                    min_sentence_length = len(ln)
        return min_sentence_length


class KanjiRatioExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        kanji_char_count = 0
        all_char_count = 0

        regex = '[一-龥]'
        pattern = re.compile(regex)

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                for char in ln:
                    if re.search(pattern, char) is not None:
                        kanji_char_count += 1
                    all_char_count += 1
        return kanji_char_count / all_char_count


class HiraganaRatioExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        hiragana_char_count = 0
        all_char_count = 0

        regex = '[ぁ-ん]'
        pattern = re.compile(regex)

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                for char in ln:
                    if re.search(pattern, char) is not None:
                        hiragana_char_count += 1
                    all_char_count += 1
        return hiragana_char_count / all_char_count


class KatakanaRatioExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        katakana_char_count = 0
        all_char_count = 0

        regex = '[ァ-ン]'
        pattern = re.compile(regex)

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                for char in ln:
                    if re.search(pattern, char) is not None:
                        katakana_char_count += 1
                    all_char_count += 1
        return katakana_char_count / all_char_count


class AlphabetRatioExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        alphabet_char_count = 0
        all_char_count = 0

        regex = '[a-xA-Z]'
        pattern = re.compile(regex)

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                for char in ln:
                    if re.search(pattern, char) is not None:
                        alphabet_char_count += 1
                    all_char_count += 1
        return alphabet_char_count / all_char_count


class NumberRatioExtractor(FeatureExtractor):

    def extract(self, post, extracted=None):
        lines = post.body.split("\n")
        number_char_count = 0
        all_char_count = 0

        regex = '[0-9]'
        pattern = re.compile(regex)

        for ln in lines:
            ln = re.sub(r"^ *", "", ln)
            if len(ln) != 0 and ln.startswith("#") is False:
                for char in ln:
                    if re.search(pattern, char) is not None:
                        number_char_count += 1
                    all_char_count += 1
        return number_char_count / all_char_count
