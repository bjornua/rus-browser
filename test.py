function(doc) {
    function rotate(size){
        if(size < 3){
            if(size == 2){
                return [[1],[0,1]];
            }
            if(size == 1){
                return [0];
            }
            return [];
        }
        a = [[size-1]];
        result = new Array();
        while(a.length !== 0){
            b = new Array();
            for(i=0; i<a.length; i++){
                for(j=1; j<a[i][0]; j++){
                    b.push([j].concat(a[i]));
                    result.push([j].concat(a[i]));
                }
                result.push([0].concat(a[i]));
            }
            a = b;
        }
        return result;
    }
    rotate(doc.tags.length).forEach(function(x){
        emit(x.map(function(x){ return lol[x]; }), null);
    });

  emit(null, doc);
}
