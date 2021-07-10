from six import iteritems

from eksisozlukbot.eksisozlukbot import spiders
from eksisozlukbot.eksisozlukbot import items
from eksisozlukbot.eksisozlukbot import middlewares
from eksisozlukbot.eksisozlukbot import pipelines
from eksisozlukbot.eksisozlukbot import settings



_SUBMODULES = {
    "spiders": spiders,
    "items": items,
    "middlewares": middlewares,
    "pipelines": pipelines,
    "settings": settings,
}

import sys

for module_name, module in iteritems(_SUBMODULES):
    sys.modules["eksisozlukbot.%s" % module_name] = module