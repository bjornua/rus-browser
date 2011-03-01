from app.utils.misc import db

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
