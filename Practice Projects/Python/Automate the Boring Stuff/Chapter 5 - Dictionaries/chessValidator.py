#this program is meant to check if a user has a valid chess 
#board.

#the "board" is a dictionary value that will hold pairs
#of keys(locations) and values (the pieces on those locations)
def isValidChessBoard(board):

    #create a list of valid names
    validNames = ["king", "queen", "knight",
                   "pawn", "bishop", "rook"]
    
    #create a list of valid letters:
    validLetters = ['a','b','c','d','e','f',
                    'g','h']
    
    #ditto for numbers:
    validNumbers = ['1','2','3','4','5','6','7','8',]
    
    #create a empty dict that will hold the amount of 
    #each piece on the board
    pieces = {}

    ### fill up the pieces dictionary. ###
    for piece in board.values():
        #for a piece at a location, check if it exists
        pieces.setdefault(piece,0)
        pieces[piece]+=1
    
    print(pieces)
    #there can only be 1 king of each type on the board.
    if pieces['bking']>1 or pieces['wking']>1:
        print("ERROR: There can only be one king of each type on the board.")
        return False

    #now loop through board to check the locations
    for loc in board.keys():
        loc = str(loc)
        #the first character in the location can range 
        #from 1 to 8
        if loc[0] not in validNumbers:
            print("ERROR: location "+str(loc)+" is not "
            "a valid alphanumeric location.")
            return False
        
        #the second character has to be from a to h
        if loc[1] not in validLetters:
            print("ERROR: location "+str(loc)+" does not "
                  "have a valid letter location.")
            return False
        

    numBPieces = 0
    numWPieces = 0
    numBPawns = 0
    numWPawns = 0

    #now check the pieces themselves
    for piece in board.values():
        
        #the name of each piece must start with a 'b' or 'w'
        if piece[0] != 'b' and piece[0] != 'w':
            print("ERROR: all pieces must start with a " \
            "b (for black) or w (for white). '" +str(piece)+ "' is not a valid piece.")
            return False
        
        #the rest of the piece's name must be one of the valid
        #names listed above
        if piece[1:] not in validNames:
            print("ERROR: pieces must have valid names. '"+str(piece)+"' is not a valid name.")
            return False
        
        #each player can only have at most 16 pieces, and 
        #at most 8 pawns
        
        #if the piece is a black piece
        if piece[0] == 'b':
            
            if piece[1:] == 'pawn': #if its a black pawn...
                numBPawns+=1

            numBPieces+=1
        else: #it's a white piece
            if piece[1:] == 'pawn': #if its a white pawn...
                numWPawns+=1

            numWPieces+=1

    print(numBPieces)
    #the number of white pieces wasn't being counted correctly because some pieces occupied the same space! 
    if numBPieces>16 or numWPieces>16:
        print("ERROR: NEITHER PLAYER CAN HAVE MORE THAN 16 PIECES.")
        return False
    
    if pieces['bpawn']>8 or pieces['wpawn']>8:
       print("ERROR: NEITHER PLAYER CAN HAVE MORE THAN 8 PAWNS")
       return False
    
    return True

testBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bpawn', '3e':
'brook', '4e':'wking', '6d':'bbishop','7d':'bbishop','8h':'bknight','8f':'bpawn','8a':'bpawn','6f':'bpawn','7e':'brook','8e':'bpawn','8d':'bpawn'
,'8b':'bpawn','7a':'bpawn','7f':'bpawn','7b':'bknight','1c':'bknight','1f':'bknight','1b':'wknight','1a':'wknight'}

res = isValidChessBoard(testBoard)
print(res)
    
    
    

        



        
        
        

