from app.utils.misc import db

from pprint import pprint

def browse_total_pages(perpage=10):
    result = db().view("rus/byname", reduce=True)
    for row in result:
        return ((row.value - 1) // perpage) + 1

def browse(page=0, perpage=10):
    skip = page * perpage
    result = db().view("rus/byname", include_docs=True, skip=skip, limit=perpage, reduce=False)
    
    for row in result:
        doc = row.doc
        
        name = doc.get("name")
        phone = doc.get("phone")
        email = doc.get("email")
        
        id = doc.id
        name = name and unicode(name)
        phone = phone and unicode(phone)
        email = email and unicode(email)
        
        yield id, name, phone, email


def info(id):
    doc = db()[id]

    name = doc.get("name")
    phone = doc.get("phone")
    email = doc.get("email")
    
    id = doc.id
    name = name and unicode(name)
    phone = phone and unicode(phone)
    email = email and unicode(email)
    
    return name, phone, email

def update(id, name, phone, email):
    doc = db()[id]

    for fieldname, fieldvalue in (
        ("name", name),
        ("phone", phone),
        ("email", email),
    ):
        if fieldvalue == None and fieldname in doc:
            del doc[fieldname]
        else:
            doc[fieldname] = fieldvalue
    db().save(doc)
