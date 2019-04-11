""" Definition of knight class and its movement. """


from .piece import Piece

class Knight(Piece):
    """ Knight model. """

    symbol = '♞'

    @property
    def movements(self):
        """ Knight moves in L shapes in all 8 directions.
        Don't mind out-of-bounds relative positions: forbidden ones will be
        silently discarded within the ``Piece.territory()`` method above.
        """
        return set([
            # Top-right movements.
            (+2, +1), (+1, +2),
            # Top-left movements.
            (-2, +1), (-1, +2),
            # Bottom-right movements.
            (+2, -1), (+1, -2),
            # Bottom-left movements.
            (-2, -1), (-1, -2),
        ])