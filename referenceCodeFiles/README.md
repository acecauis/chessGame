# Each player has 8 pieces:
#   One has black, the other white
# Pieces include:
#   - 8 Pawns
#   - 2 Rooks
#   - 2 Horses
#   - 2 Bishops
#   - 1 Queen
#   - 1 King


### RULES ###

# Each piece has their own set of moves:

#   - Pawns:  -  Can only 1 square MOVE UP, 
#             -  Moving 1 square DIAGONALLY, by being positioned diagonally exactly 1 square away from an 
#                an enemy piece, where they can COLLECT an enemy piece and replace it's position.
#             -  Cannot move up if blocked by an ememy piece

#   - Rooks:  -  Can only move in any STRAIGHT LINE any number of squares UP or SIDEWAYS
#             -  Can only COLLECT an enemy piece within any EMPTY preceding LINE of squares up to 
#             -  enemy piece

#   - Knight: -  Can only move any 4-square L SHAPE fashion, even OVER enemy and friendly pieces, finishing
#                movement at the end of L SHAPE
#             -  Can only COLLECT an enemy piece only if Knight replaces position of enemy piece 
#                at the end of L SHAPE

#   - Bishops:- 


#  -  White moves first!
#  -  Chess is recorderd as a log of the numbered moves of pieces
