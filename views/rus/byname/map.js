function(doc)  {
    if(doc.type !== "rus") return;
    
    emit([doc.name], null);
    
}

