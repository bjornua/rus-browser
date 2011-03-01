# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db, url_for
from werkzeug.utils import redirect
from pprint import pprint

import app.model.rus as rus

def browse(page=0):
    pagecount = rus.browse_total_pages(20)
    if page > pagecount - 1:
        return
    russer = rus.browse(page, 20)
    template_response("/page/index.mako",
        russer=russer,
        page=page,
        pagecount = pagecount
    )

def edit(id):
    doc = db()[id]

    template_response("/page/rus.mako",
        id=id,
        name=doc["name"],
        phone=doc["phone"],
        email=doc["email"]
    )

def save(id):
    name  = local.request.form.get("name","")
    phone = local.request.form.get("phone","")
    email = local.request.form.get("email","")

    local.response = redirect(url_for("rus.edit",id=id))
