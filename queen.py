""" Definition of queen class and its movement. """


from .piece import Piece

class Queen(Piece):
    """ Queen model. """

    symbol = '♛'

    @property
    def movements(self):
        """ Queen moves unrestricted horizontally, vertically and diagonally.
        """
        return self.horizontals | self.verticals | self.diagonals