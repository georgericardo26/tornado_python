from tornado.routing import RuleRouter, Rule, PathMatches
from tornado.web import url, Application
from core.views import MainView

from .views import AccountListView, AccountCreateView


URL_ACCOUNT = Application([
    (r"/account/create/", AccountCreateView),
    (r"/account/list/", AccountListView),
])
