import os
import json


def search_posts_dummy(query, count=100):
    data_folder = os.path.join(os.path.dirname(__file__), "../data/raw/items")
    if not os.path.isdir(data_folder):
        raise Exception("Data folder is not exist! Please prepare it (refer README.md)")
    
    posts = []
    for f in os.listdir(data_folder):
        if f.endswith(".json"):
            with open(os.path.join(data_folder, f), encoding="utf-8") as jf:
                post = json.load(jf)
                if not query:
                    posts.append(post)
                elif query and (query in post["title"] or query in post["rendered_body"]):
                    posts.append(post)
        
        if len(posts) == count:
            break
    
    return posts
