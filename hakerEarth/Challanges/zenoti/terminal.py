
def tokanise(s):
    result=[]
    sr=''
    boolflag = False
    for e in s:
        if e=='"':
            if sr !='':
                print('"'+sr+'"')
                sr=''
            boolflag=not boolflag
        if ((not boolflag and e == ' ') or e=='"'):
            if sr!='':
                print(sr)
                sr=""
        else:
            sr=sr+e
    if sr!='':
        print(sr)
    pass
s='this has "is a" test "im just Testing" hello world "so  let me test "string'
tokanise(s)