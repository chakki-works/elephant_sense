import os
import json
import numpy as np
from sklearn.externals import joblib
from scripts.features.post import Post
from scripts.features.post_feature import PostFeature
import scripts.features.length_extractor as lext
import scripts.features.charactor_extractor as cext
import scripts.features.structure_extractor as sext


class Evaluator():

    def __init__(self, model_path=""):
        self.model_path = model_path if model_path else os.path.join(os.path.dirname(__file__), "../models/")
        self.classifier = None
        self.scaler = None
        self.features = []
    
    def load(self):
        self.classifier = joblib.load(self.model_path + "banana.pkl")
        self.scaler = joblib.load(self.model_path + "banana_scaler.pkl")
        with open(self.model_path + "banana_list.txt") as f:
            self.features = f.readline().split()
        return self

    def evaluate(self, post_dict):
        if self.classifier is None:
            self.load()
        f_vector = self.get_features(post_dict)
        prediction = self.classifier.predict_proba(f_vector)
        return prediction[0][1]  # probability of good

    def get_features(self, post_dict):
        post = Post(post_dict)
        pf = PostFeature(post)
        cleaned_rendered_body = cext.RenderedBodyPreprocessor().clean_rendered_body(post.rendered_body)
        
        pf.add(lext.TitleLengthExtractor())
        pf.add(lext.SectionCountExtractor())
        pf.add(cext.KanjiRatioExtractor(cleaned_rendered_body))
        pf.add(cext.HiraganaRatioExtractor(cleaned_rendered_body))
        pf.add(cext.KatakanaRatioExtractor(cleaned_rendered_body))
        pf.add(cext.NumberRatioExtractor(cleaned_rendered_body))
        pf.add(cext.PunctuationRatioExtractor(cleaned_rendered_body))
        pf.add(lext.SentenceMeanLengthExtractor(cleaned_rendered_body))
        pf.add(lext.SentenceMeanLengthExtractor(cleaned_rendered_body))
        pf.add(lext.SentenceMaxLengthExtractor(cleaned_rendered_body))
        pf.add(sext.ImageCountExtractor())
        pf.add(sext.ImageRatioExtractor(cleaned_rendered_body))
            
        pf_d = pf.to_dict(drop_disused_feature=True)
        f_vector = []
        for f in self.features:
            f_vector.append(pf_d[f])

        f_vector = np.array(f_vector).reshape(1, -1)
        f_vector = self.scaler.transform(f_vector)
        return f_vector
