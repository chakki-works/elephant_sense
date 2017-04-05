import os
import tornado.httpserver
import tornado.ioloop
from elephant_sense import server


def main():
    http_server = tornado.httpserver.HTTPServer(server.Application())
    http_server.listen(int(os.environ.get("PORT", 8080)))
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
