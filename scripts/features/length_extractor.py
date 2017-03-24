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
