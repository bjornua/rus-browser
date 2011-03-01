# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers
import app.controllers.rus

endpoints = {
    "index": app.controllers.rus.browse,
    "rus.edit": app.controllers.rus.edit,
    "rus.save": app.controllers.rus.save,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/rus/<string:id>", "rus.edit"),
        ("POST", "/rus/<string:id>/save", "rus.save"),
        ("GET", "/browse", "index"),
        ("GET", "/browse/<int:page>", "index"),
        ("POST", "/upload_doc", "doc.upload"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)


