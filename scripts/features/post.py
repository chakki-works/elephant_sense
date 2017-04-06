class Post():

    def __init__(self, post_json):
        self.post_id = post_json["id"]
        self.annotations = post_json["annotations"]
        self.user_id = post_json["user"]["id"]
        self.user_followers_count = post_json["user"]["followers_count"]
        self.url = post_json["url"]
        self.title = post_json["title"]
        self.body = post_json["body"]
        self.rendered_body = post_json["rendered_body"]
    
    def quality(self, zero_one=True):
        score = 0
        for a in self.annotations:
            score += int(a["quality"])
        
        if not zero_one:
            return score
        else:
            if score > 1:
                return 1
            else:
                return 0
