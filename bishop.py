""" Definition of bishop class and its movement. """

from .piece import Piece

class Bishop(Piece):
    """ Bishop model. """

    symbol = '♝'

    @property
    def movements(self):
        """ Bishop moves unrestricted diagonally. """
        return self.diagonals

