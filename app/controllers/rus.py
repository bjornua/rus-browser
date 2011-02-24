# -*- coding: utf-8 -*-
from app.utils.misc import template_response, local

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
