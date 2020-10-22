from tornado.routing import RuleRouter, Rule, PathMatches
from tornado.web import url, Application
from core.views import MainView

from apps.account.urls import URL_ACCOUNT


URL_PATTERNS = RuleRouter([
    Rule(PathMatches("/account.*"), URL_ACCOUNT),
])
