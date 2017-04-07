import os
import json
from datetime import datetime
import tornado.escape
import tornado.web
from bs4 import BeautifulSoup
from elephant_sense.evaluator import Evaluator
from elephant_sense.qiita_api import search_posts


class Application(tornado.web.Application):

    def __init__(self):
        self.evaluator = Evaluator().load()
        handlers = [
            (r"/", IndexHandler),
            (r"/e/search", SearchHandler, dict(evaluator=self.evaluator)),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret=os.environ.get("SECRET_TOKEN", "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"),
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")


class SearchHandler(tornado.web.RequestHandler):

    def initialize(self, evaluator):
        self.evaluator = evaluator

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        is_debug = data["debug"]
        query = data["query"]
        message = {"posts": []}
        if is_debug:
            from elephant_sense.debug import search_posts_dummy
            posts = search_posts_dummy(query, count=30)
            posts = self.scoring(posts)
            message["posts"] = [self.trim(p) for p in posts]
            self.write(message)
        else:
            posts = search_posts(query, n=50)
            posts = self.scoring(posts)
            message["posts"] = [self.trim(p) for p in posts]
            self.write(message)
    
    @classmethod
    def trim(self, post):
        body = BeautifulSoup(post["rendered_body"], "html.parser")
        header = body.get_text()[:140]
        del post["rendered_body"]
        if "body" in post:
            del post["body"]
        post["header"] = header.strip().replace("\n", " ")
        update_time = datetime.strptime("".join(post["updated_at"].rsplit(":", 1)), "%Y-%m-%dT%H:%M:%S%z")
        post["update_time"] = update_time.strftime("%Y/%m/%d")
        return post

    def scoring(self, posts):
        scored = []
        for p in posts:
            score = self.evaluator.evaluate(p)
            p["score"] = score
            scored.append(p)
        scored = sorted(scored, key=lambda p: p["score"], reverse=True)
        return scored

    def write_json(self, message):
        serialized = json.dumps(message, ensure_ascii=False)
        self.write(serialized)
