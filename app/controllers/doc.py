# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db
from pprint import pprint
import re

from app.utils.date import nowtuple

tag_matcher = re.compile(r"([^, ]+)")
def upload():
    r = local.request
    tags = r.form.get("tags", "")
    document = r.files.get("document", None)
    
    if document.filename == None:
        template_response("/page/index.mako")
        return
    
    tags = tag_matcher.findall(tags)
    
    id_, _ = db().save({
        "type": "doc",
        "tags": tags,
        "date": nowtuple(),
    })
    db().put_attachment(db()[id_], document, "doc", "application/octet-stream")
    
    template_response("/page/index.mako")

