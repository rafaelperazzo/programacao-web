def makeBoard() :
    theboard = {};
    rows = ['top','mid','low']
    cols = ['L','M','R']
    for r in rows :
        for c in cols:
            key= str(r) + '-' + str(c)
            theBoard.setdefault(key,false)