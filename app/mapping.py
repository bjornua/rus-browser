# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers
import app.controllers.rus

endpoints = {
    "rus.browse": app.controllers.rus.browse,
    "rus.edit": app.controllers.rus.edit,
    "rus.save": app.controllers.rus.save,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/rus/<string:id>", "rus.edit"),
        ("POST", "/rus/<string:id>/save", "rus.save"),
        ("GET", "/browse", "rus.browse"),
        ("GET", "/browse/<int:page>", "rus.browse"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)


