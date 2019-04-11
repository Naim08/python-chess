""" Definition of rook class and its movement. """


from .piece import Piece

class Rook(Piece):
    """ Rook model. """

    symbol = '♜'

    @property
    def movements(self):
        """ Rook moves unrestricted horizontally and vertically. """
        return self.horizontals | self.verticals