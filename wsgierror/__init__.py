class Middleware(object):
    def __init__(self, app, global_conf):
        self.app = app

    def __call__(self, environ, start_response):
        app_iter = self.app(environ, start_response)
        try:
            return_iter = list(app_iter)
            return return_iter
        finally:
            if hasattr(app_iter, 'close'):
                app_iter.close()
