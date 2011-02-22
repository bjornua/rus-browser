# -*- coding: utf-8 -*-
import werkzeug.routing

import app.controllers
import app.controllers.doc

endpoints = {
    "index": app.controllers.index,
    "doc.upload": app.controllers.doc.upload,
    "notfound": app.controllers.notfound,
    "error": app.controllers.error,
}

url_map = werkzeug.routing.Map()

for method, path, endpoint in [
        ("GET", "/", "index"),
        ("GET", "/index", "index"),
        ("POST", "/upload_doc", "doc.upload"),
    ]:
    rule = werkzeug.routing.Rule(path, methods=[method], endpoint=endpoint)
    url_map.add(rule)


