import os
import json
from scripts.features.post import Post


class Reader():

    def __init__(self, data_folder=""):
        self.data_folder = data_folder
        if not data_folder:
            self.data_folder = os.path.join(os.path.dirname(__file__), "../../data/processed")
    
    def post_iterator(self):
        targets = []
        for f in os.listdir(self.data_folder):
            path = os.path.join(self.data_folder, f)
            if os.path.isfile(path) and f.endswith(".json"):
                targets.append(path)
        
        for t in targets:
            with open(t, mode="r", encoding="utf-8") as f:
                post_json = json.load(f)
                p = Post(post_json)
                yield p
    