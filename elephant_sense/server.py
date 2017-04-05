import os
import json
import tornado.escape
import tornado.web


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/e/search", SearchHandler),
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

    def post(self):
        is_debug = self.get_argument("debug", False)
        query = self.get_argument("query", "")
        message = {"posts": []}
        if is_debug:
            from elephant_sense.example_data import posts
            message["posts"] = posts
            self.write(json.dumps(message))
        elif not query:
            self.write(json.dumps(message))
                
        self.write(json.dumps(message))
