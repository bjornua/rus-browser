# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local, db, url_for, redirect
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
    russer = rus.info(id)
    
    template_response("/page/rus.mako",
        id=id,
        name=russer[0],
        phone=russer[1],
        email=russer[2]
    )

def save(id):
    name  = local.request.form.get("name","")
    phone = local.request.form.get("phone","")
    email = local.request.form.get("email","")
    
    if name == "":
        name = None
    if phone == "":
        phone = None
    if email == "":
        email = None

    rus.update(id, name, phone, email)

    redirect("rus.edit", id=id)
