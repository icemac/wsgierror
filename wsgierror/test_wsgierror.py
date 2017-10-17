from . import Middleware


def test_wsgierror__Middleware__1():
    """It returns the result of the app call."""
    def app(environment, start_response):
        return ["first", "second"]
    m = Middleware(app, {})
    assert ["first", "second"] == m({}, None)
