import re


class PostFeature():

    def __init__(self, post):
        self.post = post
        self._features = {}

    def add(self, feature_extractor):
        feature = feature_extractor.extract(self.post, self._features)
        key = self.to_camel(feature_extractor.__class__.__name__.replace("Extractor", ""))
        self._features[key] = feature
        return self
    
    def to_camel(self, text):
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", text)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()        

    def to_dict(self, drop_disused_feature=True):
        post_d = vars(self.post)
        post_d["quality"] = self.post.quality()
        del post_d["annotations"]

        if drop_disused_feature:
            del post_d["post_id"]
            del post_d["body"]
            del post_d["title"]
            del post_d["url"]
            del post_d["user_id"]

        for f in self._features:
            post_d[f] = self._features[f]

        return post_d
