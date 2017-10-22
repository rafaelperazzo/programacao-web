def makeBoard() :
    theboard = {};
    rows = ['top','mid','low']
    cols = ['L','M','R']
    for r in rows :
        for c in cols:
            key= str(r) + '-' + str(c)
            theBoard.setdefault(key,false)
    print ('DEBUG: '+str(theBoard))
    return theBoard
def printCell (cell):
    if cell:
        return ' '+str(cell)+' '
    else:
        return '   '
        