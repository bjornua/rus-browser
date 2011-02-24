# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers
import app.controllers.rus

endpoints = {
    "index": app.controllers.rus.browse,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/browse", "index"),
        ("GET", "/browse/<int:page>", "index"),
        ("POST", "/upload_doc", "doc.upload"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)


